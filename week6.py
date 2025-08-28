#Task 1 – Flask Blueprints & Templates
#Question: Split routes across files using Flask Blueprints, register templates/ folder for files storage, and render HTML for web pages.
#Code:
# app/__init__.py
from flask import Flask
from .routes import bp

app = Flask(__name__)
app.register_blueprint(bp)

# app/routes.py
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

# templates/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Hello, Flask Blueprints!</h1>
</body>
</html>

#Task 2 – Project Structure Best Practices
#Question: Demonstrate package layout, config & secrets, requirements & README, and testing folder for an advanced project.
#Code/Structure Example:
project/
├─ app/
│   ├─ __init__.py
│   ├─ routes.py
│   ├─ models.py
│   └─ templates/
├─ tests/
│   └─ test_app.py
├─ requirements.txt
├─ README.md
└─ main.py

#Task 3 – Dockerize Python App
#Question: Make a simple web page using HTML, CSS, and Flask, then convert the app to a Docker image and run it.
#Code:
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Flask inside Docker!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# requirements.txt
flask

# Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python","app.py"]

# Build Docker image
docker build -t flask-docker-app .

# Run container
docker run -p 5000:5000 flask-docker-app

