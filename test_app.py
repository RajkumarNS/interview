from app import app

def test_get_gists():
    client = app.test_client()
    response = client.get('/octocat')

    assert response.status_code == 200
    assert isinstance(response.json, list)
