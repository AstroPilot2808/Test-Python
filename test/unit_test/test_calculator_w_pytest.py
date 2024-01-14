import pytest

from calculator import square

def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_square_0():
    assert square(0) == 0

def test_square_str():
    with pytest.raises(TypeError):
        square("cat")