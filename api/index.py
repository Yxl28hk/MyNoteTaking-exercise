import os
import sys

# Make the repository root importable when Vercel executes this file from
# the api directory.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.main import app
