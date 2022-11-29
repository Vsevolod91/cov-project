from pytest_proj.get import get

def  test_get_for_default():
    assert get([10, 20, 34, 543, 100], 10, 5) == 5
    assert get([10, 20, 34, 543, 100], -10, 5) == 5
