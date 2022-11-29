from pytest_proj.my_slice import my_slice

def test_my_slice_2():
    assert my_slice([1, 2, 3, 4, 5, 6], 10, 4) == []
    assert my_slice([], 1, 4) == []
    assert my_slice([1, 2, 3, 4, 5, 6], -10, 4) == [1, 2, 3, 4]
    assert  my_slice([1, 2, 3, 4, 5, 6], 1, 4)
    assert  my_slice([1, 2, 3, 4, 5, 6], -2, 4) == []
    assert  my_slice([1, 2, 3, 4, 5, 6], -4, 4) == [3, 4]
    assert  my_slice([1, 2, 3, 4, 5, 6], -4) == [3, 4, 5, 6]

