import json

import pytest

from app.db import crud


def test_create_complete(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 6000.0,
        "size": 8.25,
        "title": "test_complete",
    }

    def mock_post(db, complete):
        return test_data

    monkeypatch.setattr(crud, "create_complete", mock_post)

    response = test_app.post("/completes", content=json.dumps(test_data),)
    assert response.status_code == 200
    assert response.json() == test_data


def test_create_complete_invalid_json(test_app):
    response = test_app.post("/completes", content=json.dumps({"description": "test"}))
    assert response.status_code == 422

    response = test_app.post(
        "/completes", content=json.dumps({"description": 8.25, "size": "test"})
    )
    assert response.status_code == 422


def test_read_complete(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 6000.0,
        "size": 8.25,
        "title": "test_complete",
    }

    def mock_get(db, complete_id):
        return test_data

    monkeypatch.setattr(crud, "get_complete", mock_get)

    response = test_app.get("/completes/0")
    assert response.status_code == 200
    assert response.json() == test_data
