from Sstring import make_upper  # test file name


def test_make_upper():
    assert make_upper("hello") == "HELLO"
    print("test_make_upper PASSED")

    assert make_upper("python") == "PYTHON"
    print("test_make_upper PASSED")
