import json

import pytest

from app.db import crud


def test_create_bearings(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 4900.0,
        "title": "test_bearings",
    }

    def mock_post(db, bearings):
        return test_data

    monkeypatch.setattr(crud, "create_bearings", mock_post)

    response = test_app.post("/bearings", content=json.dumps(test_data),)
    assert response.status_code == 200
    assert response.json() == test_data


def test_create_bearings_invalid_json(test_app):
    response = test_app.post("/bearings", content=json.dumps({"description": "test"}))
    assert response.status_code == 422

    response = test_app.post(
        "/bearings", content=json.dumps({"description": True, "size": "test"})
    )
    assert response.status_code == 422


def test_read_bearings(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 4900.0,
        "title": "test_bearings",
    }

    def mock_get(db, bearings_id):
        return test_data

    monkeypatch.setattr(crud, "get_bearing", mock_get)

    response = test_app.get("/bearings/0")
    assert response.status_code == 200
    assert response.json() == test_data
