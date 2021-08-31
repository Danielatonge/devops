from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    """ The function tests the root endpoint, sending a get request to
        "/" route and making sure the response status code is 200 i.e successful
    """
    response = client.get("/")
    assert response.status_code == 200
