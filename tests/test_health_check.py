from flaskr import create_app

def test_hello(client):
    response = client.get('/api/health')
    assert response.data == b'Healthy'