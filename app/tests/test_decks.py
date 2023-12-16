import json

import pytest

from app.db import crud


def test_create_deck(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 6000.0,
        "size": 8.25,
        "title": "test_deck",
    }

    def mock_post(db, deck):
        return test_data

    monkeypatch.setattr(crud, "create_deck", mock_post)

    response = test_app.post("/decks", content=json.dumps(test_data),)
    assert response.status_code == 200
    assert response.json() == test_data


def test_create_deck_invalid_json(test_app):
    response = test_app.post("/decks", content=json.dumps({"description": "test"}))
    assert response.status_code == 422

    response = test_app.post(
        "/decks", content=json.dumps({"description": 8.25, "size": "test"})
    )
    assert response.status_code == 422


def test_read_deck(test_app, monkeypatch):
    test_data = {
        "description": "test",
        "id": 0,
        "price": 6000.0,
        "size": 8.25,
        "title": "test_deck",
    }

    def mock_get(db, deck_id):
        return test_data

    monkeypatch.setattr(crud, "get_deck", mock_get)

    response = test_app.get("/decks/0")
    assert response.status_code == 200
    assert response.json() == test_data
