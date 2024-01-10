from minitorch.operators import mul, id, add, neg, lt, eq, max

def test_id():
    assert id(5) == 5, "Test case 1 failed"
    assert id(0) == 0, "Test case 2 failed"
    assert id(-10) == -10, "Test case 3 failed"

def test_add():
    assert add(2, 3) == 5, "Test case 1 failed"
    assert add(-5, 10) == 5, "Test case 2 failed"
    assert add(0, 0) == 0, "Test case 3 failed"

def test_neg():
    assert neg(5) == -5, "Test case 1 failed"
    assert neg(-10) == 10, "Test case 2 failed"
    assert neg(0) == 0, "Test case 3 failed"


def test_lt():
    assert lt(2, 3) == 1.0, "Test case 1 failed"
    assert lt(5, 2) == 0.0, "Test case 2 failed"
    assert lt(0, 0) == 0.0, "Test case 3 failed"

def test_eq():
    assert eq(5, 5) == 1.0, "Test case 1 failed"
    assert eq(10, 5) == 0.0, "Test case 2 failed"
    assert eq(0, 0) == 1.0, "Test case 3 failed"

def test_max():
    assert max(2, 3) == 3.0, "Test case 1 failed"
    assert max(5, 2) == 5.0, "Test case 2 failed"
    assert max(0, 0) == 0.0, "Test case 3 failed"

# Run the tests
test_lt()
test_eq()
test_max()

# Run the tests
test_id()
test_add()
test_neg()

print("All correct")

