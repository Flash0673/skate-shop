import json

import pytest

from app.db import crud


def test_create_griptape(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 1000.0,
        "title": "test_griptape",
        "length": 24.0,
        "width": 15.0
    }

    def mock_post(db, griptape):
        return test_data

    monkeypatch.setattr(crud, "create_griptape", mock_post)

    response = test_app.post("/griptapes", content=json.dumps(test_data),)
    assert response.status_code == 200
    assert response.json() == test_data


def test_create_griptape_invalid_json(test_app):
    response = test_app.post("/griptapes", content=json.dumps({"description": "test"}))
    assert response.status_code == 422

    response = test_app.post(
        "/griptapes", content=json.dumps({"description": False, "size": "test"})
    )
    assert response.status_code == 422


def test_read_griptape(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 1000.0,
        "title": "test_griptape",
        "length": 24.0,
        "width": 15.0
    }

    def mock_get(db, griptape_id):
        return test_data

    monkeypatch.setattr(crud, "get_griptape", mock_get)

    response = test_app.get("/griptapes/0")
    assert response.status_code == 200
    assert response.json() == test_data
