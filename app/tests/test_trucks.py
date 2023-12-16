import json

import pytest

from app.db import crud


def test_create_trucks(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 6000.0,
        "size": 5.5,
        "title": "test_truck",
        "quantity": 2,
        "has_bushing": True,
    }

    def mock_post(db, truck):
        return test_data

    monkeypatch.setattr(crud, "create_truck", mock_post)

    response = test_app.post("/trucks", content=json.dumps(test_data),)
    assert response.status_code == 200
    assert response.json() == test_data


def test_create_trucks_invalid_json(test_app):
    response = test_app.post("/trucks", content=json.dumps({"description": "test"}))
    assert response.status_code == 422

    response = test_app.post(
        "/trucks", content=json.dumps({"has_bushing": 5, "size": "test"})
    )
    assert response.status_code == 422


def test_read_trucks(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 6000.0,
        "size": 5.5,
        "title": "test_truck",
        "quantity": 2,
        "has_bushing": True,
    }

    def mock_get(db, truck_id):
        return test_data

    monkeypatch.setattr(crud, "get_truck", mock_get)

    response = test_app.get("/trucks/0")
    assert response.status_code == 200
    assert response.json() == test_data
