from src.math_operations import add, subtract

def test_add():
    assert add(2,4)==6
    assert add(10,5)==15
    assert add(-5,-3)==-8
    assert add(-1,1)==0

def test_subtract():
    assert subtract(4,2)==2
    assert subtract(15,10)==5
    assert subtract(-3,-5)==-2
    assert subtract(-1,-1)==0