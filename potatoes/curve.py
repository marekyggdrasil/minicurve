import numpy as np

from potatoes.helpers import extendedEuclideanAlgorithm
from potatoes.helpers import inverse
from potatoes.mod_sqrt import modular_sqrt


class Potatoes:
    def __init__(self, a, b, p, tracing=False):
        self.a = a
        self.b = b
        self.p = p

        self.x = None
        self.y = None

        self.tracing = tracing
        self.rxs = []
        self.rys = []

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setTracing(self, rxs, rys):
        self.rxs = rxs
        self.rys = rys
        self.tracing = True

    def getAll(self):
        points = []
        for x in range(self.p):
            y_squared = np.mod(x**3 + self.a*X + self.b, self.p)
            residue_1 = modular_sqrt(y_squared, self.p)
            residue_2 = self.p - residue_1
            points.append(tuple(x, residue_1))
            points.append(tuple(x, resicue_2))
        return points

    def __add__(self, other):
        if other.a != self.a \
           or other.b != self.b \
           or other.p != self.p:
            raise ValueError('Incompatible curves')
        rx, ry = self.eccFiniteAddition(
            self, self.x, self.y, other.x, other.y, self.a, self.b, self.p)
        res = Potatoes(self.a, self.b, self.p)
        res.setX(rx)
        res.setY(ry)
        return res

    def __mul__(self, other):
        if not isinstance(other, int):
            raise ValueError('ECC point can only be multiplied by a scalar')
        rxs, rys, rx, ry = eccScalarMult(other, self.x, self.y, self.a, self.b, self.p)
        res = Potatoes(self.a, self.b, self.p, tracing=self.tracing)
        res.setX(rx)
        res.setY(ry)
        if self.tracing:
            res.setTracing(rxs, rys)
        return res

    @classmethod
    def onCurve(self, X, Y, a, b, p):
        # None is the infinity point
        if X is None and Y is None:
            return True
        return np.mod(Y**2 - X**3 - a*X - b, p) == 0

    @classmethod
    def eccFiniteAddition(self, Px, Py, Qx, Qy, a, b, p):
        if None in [Px, Py]:
            return Qx, Qy
        if None in [Qx, Qy]:
            return Px, Py
        assert self.onCurve(Px, Py, a, b, p)
        assert self.onCurve(Qx, Qy, a, b, p)
        if Px == Qx and Py != Qy:
            # point1 + (-point1) = 0
            return None, None
        if Px == Qx:
            m = (3*Px**2 + a)*inverse(2*Py, p)
        else:
            m = (Py - Qy)*inverse(Px - Qx, p)
        Rx = np.mod(m**2 - Px - Qx, p)
        Ry = np.mod(-(Py + m*(Rx - Px)), p)
        assert onCurve(Rx, Ry, a, b, p)
        return Rx, Ry

    @classmethod
    def eccNegation(self, Px, Py, a, b, p):
        assert self.onCurve(Px, Py, a, b, p)
        Rx = Px
        Ry = np.mod(-Py, p)
        assert self.onCurve(Rx, Ry, a, b, p)
        return Rx, Ry

    @classmethod
    def eccScalarMult(k, Px, Py, a, b, p):
        assert self.onCurve(Px, Py, a, b, p)
        if np.mod(k, p) == 0:
            return [], [], None, None
        if k < 0:
            # k * point = -k * (-point)
            Rx, Ry = self.eccNegation(Px, Py)
            return self.eccScalarMult(-k, Rx, Ry)
        rx, ry = Px, Py
        Rxs, Rys = [rx], [ry]
        for i in range(k-1):
            rx, ry = self.eccFiniteAddition(rx, ry, Px, Py, a, b, p)
            assert self.onCurve(rx, ry, a, b, p)
            Rxs.append(rx)
            Rys.append(ry)
        return Rxs, Rys, rx, ry

    @classmethod
    def generateGroup(Gx, Gy, a, b, p):
        Qx, Qy = Gx, Gy
        orbit = [(0, 0)]
        while (not (Qx == 0 and Qy == 0)) and (None not in [Qx, Qy]):
            point = tuple([Qx, Qy])
            orbit.append(point)
            Qx, Qy = self.eccFiniteAddition(Qx, Qy, Gx, Gy, a, b, p)
        return orbit

    @classmethod
    def bruteForceKey(Px, Py, pub_x, pub_y, a, b, p):
        for k in range(p):
            _, _, public_x, public_y = self.eccScalarMult(k, Px, Py, a, b, p)
            if public_x == pub_x and public_y == pub_y:
                return k
