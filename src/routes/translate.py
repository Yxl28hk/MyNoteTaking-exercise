import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from dotenv import load_dotenv
from flask import Blueprint, jsonify, request

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

translate_bp = Blueprint('translate', __name__)


def _extract_translation(response_data):
    choices = response_data.get('choices')
    if not isinstance(choices, list) or not choices:
        raise ValueError('The language model returned no choices')

    message = choices[0].get('message')
    if not isinstance(message, dict):
        raise ValueError('The language model returned no message')

    content = message.get('content')
    if isinstance(content, str):
        translated_text = content.strip()
    elif isinstance(content, list):
        translated_text = ''.join(
            item.get('text', '') for item in content
            if isinstance(item, dict) and isinstance(item.get('text'), str)
        ).strip()
    else:
        translated_text = ''

    if not translated_text:
        refusal = message.get('refusal')
        if refusal:
            raise ValueError(f'The language model refused the request: {refusal}')
        raise ValueError('The language model returned empty content')
    return translated_text


@translate_bp.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json(silent=True) or {}
    text = data.get('text', '').strip()
    source_language = data.get('source_language', 'Auto-detect').strip()
    target_language = data.get('target_language', '').strip()

    if not text:
        return jsonify({'error': 'Text to translate is required'}), 400
    if not target_language:
        return jsonify({'error': 'Target language is required'}), 400
    if len(text) > 20000:
        return jsonify({'error': 'Text must be 20,000 characters or fewer'}), 400

    token = os.getenv('OPENROUTER_API_KEY', '').strip()
    if not token:
        return jsonify({'error': 'OPENROUTER_API_KEY is not configured on the server'}), 503

    model = os.getenv('OPENROUTER_MODEL', 'nvidia/nemotron-3-ultra-550b-a55b:free')
    prompt = (
        f'Translate the following text from {source_language} to {target_language}. '
        'Preserve the original meaning, formatting, paragraph breaks, and tone. '
        'Return only the translated text without explanations or quotation marks.\n\n'
        f'{text}'
    )
    payload = {
        'model': model,
        'messages': [
            {
                'role': 'system',
                'content': 'You are a professional translator.',
            },
            {'role': 'user', 'content': prompt},
        ],
        'temperature': 0.2,
    }
    api_request = Request(
        'https://openrouter.ai/api/v1/chat/completions',
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'HTTP-Referer': os.getenv('OPENROUTER_SITE_URL', 'http://localhost:5001'),
            'X-Title': os.getenv('OPENROUTER_SITE_NAME', 'NoteTaker'),
        },
        method='POST',
    )

    try:
        with urlopen(api_request, timeout=60) as response:
            response_data = json.loads(response.read().decode('utf-8'))
        translated_text = _extract_translation(response_data)
        return jsonify({'translation': translated_text})
    except HTTPError as error:
        try:
            details = json.loads(error.read().decode('utf-8')).get('message')
        except (ValueError, UnicodeDecodeError):
            details = None
        return jsonify({'error': details or 'Translation provider request failed'}), 502
    except (URLError, TimeoutError):
        return jsonify({'error': 'Unable to reach the translation provider'}), 502
    except (KeyError, IndexError, TypeError, ValueError) as error:
        return jsonify({'error': str(error)}), 502
