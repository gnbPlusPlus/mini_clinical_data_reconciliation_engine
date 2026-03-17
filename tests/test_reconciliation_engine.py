from backend.services.reconciliation_engine import reconcile_medication

# Test the mock LLM response for medication reconciliation
def test_reconciliation_engine_mocked(reconciliation_data):
    patient_context = reconciliation_data.get("patient_context")
    sources = reconciliation_data.get("sources")

    result = reconcile_medication(patient_context, sources)

    assert result["reconciled_medication"] == "Metformin 500mg twice daily"
    assert result["confidence_score"] == 0.88
    assert "reasoning" in result
    assert len(result["recommended_actions"]) == 2
    assert result["clinical_safety_check"] == "PASSED"