# main.py
from flask import Flask
from src.pylong.api.routes import case_routes
from src.pylong.api.routes import test_routes
from flask_cors import CORS

app = Flask(__name__)

# CORS(app)
CORS(app, resources=r'/*', supports_credentials=True)

# register routes
app.register_blueprint(case_routes, url_prefix='/api/case')
app.register_blueprint(test_routes, url_prefix='/api/test')


# src/main.py
@app.after_request
def add_header(response):
    return response
