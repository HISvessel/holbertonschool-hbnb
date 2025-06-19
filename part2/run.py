"""this file is the entry point of the application
runs the app along with the corresponding files:
pending tests"""
from app.api import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
