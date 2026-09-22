from calculator import add


def test_add():  # Test function name
    assert add(2, 3) == 5  # Checks if the sum is correct
    assert add(-1, 1) == 0  # Checks if the sum is correct
    assert add(-1, -1) == -2  # Checks if the sum is correct
