import json, pytest
from flask import Flask

from backend.services.reconciliation_engine import reconcile_medication
from backend.services.validation_engine import validate_data_quality
from backend.services.llm_service import generate_reconciliation_reasoning, generate_data_quality_scores
from backend.routes.reconcile import reconcile_bp
from backend.routes.validate import validate_bp

# Helper to load JSON files
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
@pytest.fixture
def client():
    app = Flask(__name__)

    app.register_blueprint(reconcile_bp, url_prefix='/api/reconcile')
    app.register_blueprint(validate_bp, url_prefix='/api/validate')

    with app.test_client() as client:
        yield client

@pytest.fixture
def reconciliation_data():
    return load_json('tests/sample_data/reconcile_example.json')

@pytest.fixture
def validation_data():
    return load_json('tests/sample_data/validate_example.json')