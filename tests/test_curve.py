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
    P = Potatoes(a, b, p, x=3, y=2)
    Q = Potatoes(a, b, p, x=6, y=5)
    R = P + Q
    assert R.x == 6
    assert R.y == 2

def test_curve_scalar_multiplication():
    a = 0
    b = 5
    p = 7
    P = Potatoes(a, b, p, x=3, y=2)
    Q = Potatoes(a, b, p, x=6, y=5)
    R = Potatoes(a, b, p, x=3, y=5)
    assert P*3 == Q
    assert 3*P == Q
    assert -1*P == R
    assert P*(-1) == R
