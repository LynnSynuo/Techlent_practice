from app.src.calculator import Calculator

#initialized
cal = Calculator()

def test_add():
    #use assert to test if the statement is True or not
    # if not True, it'll report
    assert cal.add(1, 1) == 2
    assert cal.add(1, 2) == 3

def test_subtract():
    assert cal.subtract(3, 1) == 2
    assert cal.subtract(10, 3) == 7
    assert cal.subtract(100, 2) == 98
