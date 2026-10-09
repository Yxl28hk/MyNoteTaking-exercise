# NoteTaker - Personal Note Management Application

A modern, responsive web application for managing personal notes with a beautiful user interface and full CRUD functionality.

## 🌟 Features

- **Create Notes**: Add new notes with titles and rich content
- **Edit Notes**: Update existing notes with real-time editing
- **Delete Notes**: Remove notes you no longer need
- **Search Notes**: Find notes quickly by searching titles and content
- **Auto-save**: Notes are automatically saved as you type
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Modern UI**: Beautiful gradient design with smooth animations
- **Real-time Updates**: Instant feedback and updates

## 🚀 Live Demo

The application is deployed and accessible at: **https://3dhkilc88dkk.manus.space**

## 🛠 Technology Stack

### Frontend
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript (ES6+)**: Interactive functionality and API communication

### Backend
- **Python Flask**: Web framework for API endpoints
- **SQLAlchemy**: ORM for database operations
- **Flask-CORS**: Cross-origin resource sharing support

### Database
- **Neon PostgreSQL**: External managed database for stateless deployments

## 📁 Project Structure

```
notetaking-app/
├── src/
│   ├── models/
│   │   ├── user.py          # User model (template)
│   │   └── note.py          # Note model with database schema
│   ├── routes/
│   │   ├── user.py          # User API routes (template)
│   │   └── note.py          # Note API endpoints
│   ├── static/
│   │   ├── index.html       # Frontend application
│   │   └── favicon.ico      # Application icon
│   └── main.py              # Flask application entry point
├── venv/                    # Python virtual environment
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🔧 Local Development Setup

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation Steps

1. **Clone or download the project**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**
   ```bash
   source venv/bin/activate
   ```

   Remark: On Windows, use `venv\Scripts\activate`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python src/main.py
   ```

5. **Access the application**
   - Open your browser and go to `http://localhost:5001`

## 📡 API Endpoints

### Notes API
- `GET /api/notes` - Get all notes
- `POST /api/notes` - Create a new note
- `GET /api/notes/<id>` - Get a specific note
- `PUT /api/notes/<id>` - Update a note
- `DELETE /api/notes/<id>` - Delete a note
- `GET /api/notes/search?q=<query>` - Search notes
- `POST /api/translate` - Translate note content with OpenRouter

Translation request:
```json
{
  "text": "要翻译的内容",
  "source_language": "Chinese",
  "target_language": "English"
}
```

The response is `{ "translation": "..." }`. The API key is only read by the
Flask server and is never sent to the browser.

### Request/Response Format
```json
{
  "id": 1,
  "title": "My Note Title",
  "content": "Note content here...",
  "created_at": "2025-09-03T11:26:38.123456",
  "updated_at": "2025-09-03T11:27:30.654321"
}
```

## 🎨 User Interface Features

### Sidebar
- **Search Box**: Real-time search through note titles and content
- **New Note Button**: Create new notes instantly
- **Notes List**: Scrollable list of all notes with previews
- **Note Previews**: Show title, content preview, and last modified date

### Editor Panel
- **Title Input**: Edit note titles
- **Content Textarea**: Rich text editing area
- **Save Button**: Manual save option (auto-save also available)
- **Delete Button**: Remove notes with confirmation
- **AI Translation**: Translate note content into another language and optionally replace the current content
- **Real-time Updates**: Changes reflected immediately

### Design Elements
- **Gradient Background**: Beautiful purple gradient backdrop
- **Glass Morphism**: Semi-transparent panels with backdrop blur
- **Smooth Animations**: Hover effects and transitions
- **Responsive Layout**: Adapts to different screen sizes
- **Modern Typography**: Clean, readable font stack

## 🔒 Database Schema

### Notes Table
```sql
CREATE TABLE note (
    id INTEGER PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## 🚀 Deployment

The application is configured for easy deployment with:
- CORS enabled for cross-origin requests
- Host binding to `0.0.0.0` for external access
- Production-ready Flask configuration
- Persistent external Neon PostgreSQL database

### Deploy to Vercel

This repository includes a Vercel Python Function entry point at
`api/index.py` and the routing configuration in `vercel.json`.

1. Import the repository into Vercel.
2. In **Project Settings → Environment Variables**, add the following
   variables for every environment where the app will run:

   ```env
   DATABASE_URL=your-Neon-PostgreSQL-connection-string
   SECRET_KEY=your-long-random-secret
   OPENROUTER_API_KEY=your-OpenRouter-key
   ```

   `OPENROUTER_API_KEY` is only required if the translation feature is used.
   Use a Neon connection string with `sslmode=require`.
3. Deploy or redeploy the project. Do not upload `.env`; it is intentionally
   excluded from version control.

Vercel runs the Flask application as a Python Function. The application
creates the database tables on startup, so the configured database user must
have permission to create tables.

## 🔧 Configuration

### Environment Variables
- `FLASK_ENV`: Set to `development` for debug mode
- `SECRET_KEY`: Flask secret key for sessions
- `OPENROUTER_API_KEY`: OpenRouter API key (required for translation)
- `OPENROUTER_MODEL`: Optional OpenRouter model name (defaults to `nvidia/nemotron-3-ultra-550b-a55b:free`)
- `OPENROUTER_SITE_URL`: Optional site URL sent to OpenRouter for rankings
- `OPENROUTER_SITE_NAME`: Optional app name sent to OpenRouter

### Database Configuration
- `DATABASE_URL`: Neon PostgreSQL connection string (required)
- `SECRET_KEY`: Flask secret key (required in production)
- Tables are created automatically on startup through SQLAlchemy
- No note data is stored on the application filesystem

#### Neon setup

1. Create a project at [Neon](https://neon.tech/).
2. Open the project's **Connect** dialog and copy the pooled connection string.
3. Put it in `.env`:

```env
DATABASE_URL=postgresql://USER:PASSWORD@HOST/DBNAME?sslmode=require
SECRET_KEY=replace-with-a-long-random-value
```

The application converts `postgresql://` to the `psycopg` SQLAlchemy driver
automatically. Keep `.env` private and never commit database credentials.

## 📱 Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues or questions:
1. Check the browser console for error messages
2. Verify the Flask server is running
3. Ensure all dependencies are installed
4. Check network connectivity for the deployed version

## 🎯 Future Enhancements

Potential improvements for future versions:
- User authentication and multi-user support
- Note categories and tags
- Rich text formatting (bold, italic, lists)
- File attachments
- Export functionality (PDF, Markdown)
- Dark/light theme toggle
- Offline support with service workers
- Note sharing capabilities

---

**Built with ❤️ using Flask, Neon PostgreSQL, and modern web technologies**
