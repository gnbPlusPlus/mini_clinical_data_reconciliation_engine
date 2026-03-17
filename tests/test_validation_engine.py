from backend.services.validation_engine import validate_data_quality

# Test the mock LLM response for data quality validation
def test_validation_engine_mocked(validation_data):
    demographics = validation_data.get("demographics")
    medications = validation_data.get("medications")
    allergies = validation_data.get("allergies")
    conditions = validation_data.get("conditions")
    vital_signs = validation_data.get("vital_signs")
    last_updated = validation_data.get("last_updated")

    result = validate_data_quality(demographics, medications, allergies, conditions, vital_signs, last_updated)

    assert result["overall_score"] == 62
    assert result["breakdown"]["completeness"] == 60
    assert result["breakdown"]["accuracy"] == 50
    assert result["breakdown"]["timeliness"] == 70
    assert result["breakdown"]["clinical_plausibility"] == 40
    assert len(result["issues_detected"]) == 3
    assert result["issues_detected"][0]["severity"] == "medium"
    assert result["issues_detected"][1]["severity"] == "high"
    assert result["issues_detected"][2]["severity"] == "medium"