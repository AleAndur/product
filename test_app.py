from app import greet_user

def test_greet_user(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: "John")

    assert greet_user() == "Hello John"
