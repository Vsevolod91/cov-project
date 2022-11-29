from pytest_proj.get import get

def test_get_for_none_default():
    assert get([1, 10, 15, 8, 25], -4) == None
    assert get([1, 10, 15, 8, 25], 10) == None
