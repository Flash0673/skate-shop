import json

import pytest

from app.db import crud


def test_create_wheels(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 3500.0,
        "size": 52,
        "title": "test_wheels",
        "hardness": "99A",
        "color": "green"
    }

    def mock_post(db, wheels):
        return test_data

    monkeypatch.setattr(crud, "create_wheels", mock_post)

    response = test_app.post("/wheels", content=json.dumps(test_data),)
    assert response.status_code == 200
    assert response.json() == test_data


def test_create_wheels_invalid_json(test_app):
    response = test_app.post("/wheels", content=json.dumps({"description": "test"}))
    assert response.status_code == 422

    response = test_app.post(
        "/wheels", content=json.dumps({"description": True, "size": "test"})
    )
    assert response.status_code == 422


def test_read_wheels(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 3500.0,
        "size": 52,
        "title": "test_wheels",
        "hardness": "99A",
        "color": "green"
    }

    def mock_get(db, wheels_id):
        return test_data

    monkeypatch.setattr(crud, "get_wheel", mock_get)

    response = test_app.get("/wheels/0")
    assert response.status_code == 200
    assert response.json() == test_data
