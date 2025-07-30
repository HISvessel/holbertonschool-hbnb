"""this file is the entry point of the application
runs the app along with the corresponding files:
pending tests"""
from app import create_app
from flask_cors import CORS


app = create_app()
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
