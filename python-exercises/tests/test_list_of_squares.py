import pytest
from applications import list_of_squares





def test_list_square_12():
    assert list_of_squares.list_of_squares(12) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

def test_list_small():
    assert list_of_squares.list_of_squares(9) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
    