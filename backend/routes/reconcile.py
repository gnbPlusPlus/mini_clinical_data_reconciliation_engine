from flask import Blueprint, request, jsonify
from backend.services.reconciliation_engine import reconcile_medication

reconcile_bp = Blueprint('reconcile', __name__)

# POST route for /api/reconcile/medication
@reconcile_bp.route('/medication', methods=['POST'])
def reconcile_medication_route():
    data = request.get_json()

    # Validate input types
    if not data:
        return jsonify({"error": "Invalid JSON input."}), 400

    patient_context = data.get('patient_context')
    sources = data.get('sources')

    if not isinstance(patient_context, dict):
        return jsonify({"error": "Patient context must be a dictionary."}), 400
    if not isinstance(sources, list):
        return jsonify({"error": "Sources must be a list (of dictionaries)."}), 400

    # Validate that the source contains the required keys
    required_source_keys = ["system", "medication", "source_reliability"]
    for source in sources:
        if not all(key in source for key in required_source_keys):
            return jsonify({"error": "Each source must contain 'system', 'medication', and 'source_reliability' keys."}), 400

    reconciliation_result = reconcile_medication(patient_context, sources)

    return jsonify(reconciliation_result)