def test_reconcile_route_success(client, reconciliation_data):
    response = client.post('/api/reconcile/medication', json=reconciliation_data)
    assert response.status_code == 200

def test_reconcile_route_invalid_patient_context(client):
    response = client.post('/api/reconcile/medication', json={
        "patient_context": "not a dict",
        "sources": []
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data