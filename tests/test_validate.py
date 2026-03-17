def test_validate_route_success(client, validation_data):
    response = client.post('/api/validate/data-quality', json=validation_data)
    assert response.status_code == 200

def test_validate_route_invalid_demographics(client):
    response = client.post('/api/validate/data-quality', json={
        "demographics": "not a dict",
        "medications": [],
        "allergies": [],
        "conditions": [],
        "vital_signs": {},
        "last_updated": "2024-06-15"
    })
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data