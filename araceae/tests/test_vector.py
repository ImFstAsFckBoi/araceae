from ..vector import Vec, Vec2, Vec3, euclidean, manhattan
from math import sqrt, cos, sin, pi
from random import randrange
from numpy import array
from pytest import raises


def test_distance_euclidean():
    assert Vec2(3, 4).euclidean() == 5.0

    for _ in range(10):
        x, y = randrange(-10, 10), randrange(-10, 10)
        assert sqrt(x**2 + y**2) == Vec2(x, y).euclidean()

    for _ in range(10):
        x, y, z = randrange(-10, 10), randrange(-10, 10), randrange(-10, 10)
        assert sqrt(x**2 + y**2 + z**2) == Vec3(x, y, z).euclidean()

    for _ in range(10):
        a, b = randrange(-10, 10), randrange(-10, 10)
        c, d = randrange(-10, 10), randrange(-10, 10)
        v = Vec(a, b, c, d).euclidean()
        assert sqrt(a**2 + b**2 + c**2 + d**2) == v


def test_distance_manhattan():
    assert Vec2(10, 10).manhattan() == 20
    # assert Vec2(-1, 2).manhattan() == 3

    for _ in range(10):
        x, y = randrange(-10, 10), randrange(-10, 10)
        assert abs(x) + abs(y) == Vec2(x, y).manhattan()

    for _ in range(10):
        x, y, z = randrange(-10, 10), randrange(-10, 10), randrange(-10, 10)
        assert abs(x) + abs(y) + abs(z) == Vec3(x, y, z).manhattan()

    for _ in range(10):
        a, b = randrange(-10, 10), randrange(-10, 10)
        c, d = randrange(-10, 10), randrange(-10, 10)
        v = Vec(a, b, c, d).manhattan()
        assert abs(a) + abs(b) + abs(c) + abs(d) == v


def test_diff_distance():
    a = Vec3(-1, -1, -1)
    b = Vec3(2, 2, 2)

    assert euclidean(a, b) == 3*sqrt(3)
    assert manhattan(a, b) == 9

    u = Vec2(1, 6)
    v = Vec2(5, 2)

    assert euclidean(u, v) == 4*sqrt(2)
    assert manhattan(u, v) == 8


def test_iter():
    a = Vec2(1, 2)
    b = Vec3(1, 2, 3)
    c = Vec(1, 2, 3, 4)

    assert tuple(a) == (1, 2)
    assert tuple(b) == (1, 2, 3)
    assert tuple(c) == (1, 2, 3, 4)


def test_matmul():
    v = Vec2(1, 2)
    u = Vec3(1, 2, 3)
    w = Vec2(1, 0)

    M1 = array([[-2, 0],
                [0, -2]])

    M2 = array([[-3, 0, 0],
                [0, 3, 0],
                [0, 0, -3]])

    M3 = array([[cos(-pi/4), -sin(-pi/4)],
                [sin(-pi/4), cos(-pi/4)]]) * (2/sqrt(2))

    assert tuple(v.matmul(M1)) == (-2, -4)
    assert tuple(u.matmul(M2)) == (-3, 6, -9)
    assert tuple(map(round, w.matmul(M3))) == (1, 1)


def test_compare():
    v = Vec2(1, 1)
    u = Vec2(1, 1)
    w = Vec2(2, 2)

    assert w > u
    assert w >= u
    assert v >= u
    assert v < w
    assert v <= w
    assert v <= u
    assert v == u
    assert v == u

    assert v == (1, 1)
    assert v != (2, 2)


def test_immediate_op():
    x = Vec2(0, 0)
    assert x == (0, 0)
    x += Vec2(1, 1)
    assert x == (1, 1)
    x -= (1, 1)
    assert x == (0, 0)

    with raises(AssertionError):
        x += (1, 2, 3)
