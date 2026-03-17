from flask import Blueprint, request, jsonify
from datetime import datetime
from backend.services.validation_engine import validate_data_quality

validate_bp = Blueprint('validate', __name__)

# POST route for /api/validate/data-quality
@validate_bp.route('/data-quality', methods=['POST'])
def validate_data_quality_route():
    data = request.get_json()

    # Validate input types
    if not data:
        return jsonify({"error": "Invalid JSON input."}), 400

    demographics = data.get('demographics')
    medications = data.get('medications')
    allergies = data.get('allergies')
    conditions = data.get('conditions')
    vital_signs = data.get('vital_signs')
    last_updated = data.get('last_updated')

    if not isinstance(demographics, dict):
        return jsonify({"error": "Patient context must be a dictionary."}), 400
    if not isinstance(medications, list):
        return jsonify({"error": "Medications must be a list."}), 400
    if not isinstance(allergies, list):
        return jsonify({"error": "Allergies must be a list."}), 400
    if not isinstance(conditions, list):
        return jsonify({"error": "Conditions must be a list."}), 400
    if not isinstance(vital_signs, dict):
        return jsonify({"error": "Vital signs must be a dictionary."}), 400
    if not isinstance(last_updated, str) and not isinstance(last_updated, datetime.datetime):
        return jsonify({"error": "Last updated must be a string or datetime object."}), 400

    validation_result = validate_data_quality(demographics, medications, allergies, conditions, vital_signs, last_updated)

    return jsonify(validation_result)
