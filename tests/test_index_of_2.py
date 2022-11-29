from pytest_proj.index_of import index_of

def test_index_of_2():
    assert index_of([], 10, 1) == -1
    assert index_of([10, 15, 25, 40, 55, 60], 40, -10) == 3
    assert index_of([10, 15, 25, 40, 55, 60], 40, -4) == 3
    assert index_of([10, 15, 25, 40, 55, 60], 100) == -1
    assert index_of([10, 15, 25, 40, 55, 60], 100, -2) == -1
    assert index_of([10, 15, 25, 40, 55, 60], 100, -10) == -1
