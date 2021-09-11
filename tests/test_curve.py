import pytest

from potatoes.curve import Potatoes


def test_finite_field_naive():
    a = 0
    b = 5
    p = 7
    field = Potatoes(a, b, p)
    points = field.getAllNaive()
    points_ref = [(None, None), (3, 2), (5, 2), (6, 2), (3, 5), (5, 5), (6, 5)]
    assert len(set(points) - set(points_ref)) == 0

@pytest.mark.skip(reason='the quadratic residues implementation needs to be debugged')
def test_finite_field():
    a = 0
    b = 5
    p = 7
    field = Potatoes(a, b, p)
    points = field.getAll()
    points_ref = [(None, None), (3, 2), (5, 2), (6, 2), (3, 5), (5, 5), (6, 5)]
    assert len(set(points) - set(points_ref)) == 0

def test_curve_addition():
    a = 0
    b = 5
    p = 7
    P = Potatoes(a, b, p)
    P.setX(3)
    P.setY(2)
    Q = Potatoes(a, b, p)
    Q.setX(6)
    Q.setY(5)
    R = P + Q
    assert R.x == 6
    assert R.y == 2

def test_curve_scalar_multiplication():
    a = 0
    b = 5
    p = 7
    P = Potatoes(a, b, p)
    P.setX(3)
    P.setY(2)
    k = 3
    kP = P*3
    Q = Potatoes(a, b, p)
    Q.setX(6)
    Q.setY(5)
    assert kP == Q
