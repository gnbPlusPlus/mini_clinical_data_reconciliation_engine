from backend.services.llm_service import generate_data_quality_scores

# Function that accepts a patient record and returns a data quality validation report
def validate_data_quality(demographics, medications, allergies, conditions, vital_signs, last_updated):
    # Consolidate fields into a single patient record dict to pass to the LLM
    patient_record = {
        "demographics": demographics,
        "medications": medications,
        "allergies": allergies,
        "conditions": conditions,
        "vital_signs": vital_signs,
        "last_updated": last_updated
    }

    validation_report = generate_data_quality_scores(patient_record)

    return validation_report