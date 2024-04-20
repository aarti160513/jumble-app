def test_request_jumble_shift100(client):
    response = client.post("/api/jumble/100", json={
            "message": "tes%%^&&**t 123!"
    })
    
    assert response.json["jumbled"] ==  "paop 123"


def test_request_jumble_shift1(client):
    response = client.post("/api/jumble/1", json={
            "message": "test 123!"
    })
    
    assert response.json["jumbled"] ==  "uftu 123"


def test_request_jumble_shift0(client):
    response = client.post("/api/jumble/0", json={
            "message": "test 123!"
    })
    
    assert response.json["jumbled"] ==  "test 123"