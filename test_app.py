from app import app

def test_config_endpoint():
    with app.test_client() as client:
        response = client.get("/config")
        assert response.status_code == 200
        data = response.get_json()
        assert "highlight_recent" in data
        assert "heatmap_column" in data

def test_data_endpoint():
    with app.test_client() as client:
        response = client.get("/data")
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert all("name" in row and "score" in row and "timestamp" in row for row in data)
