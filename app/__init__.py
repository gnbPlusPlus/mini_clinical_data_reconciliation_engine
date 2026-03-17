from flask import Flask
from flask_cors import CORS
from backend.routes.reconcile import reconcile_bp
from backend.routes.validate import validate_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register blueprints
    app.register_blueprint(reconcile_bp, url_prefix='/api/reconcile')
    app.register_blueprint(validate_bp, url_prefix='/api/validate')

    return app