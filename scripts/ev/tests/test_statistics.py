from pytest import approx
from ..statistics import weibull


def test_weibull():
    w = weibull(0, 2, 20)
    assert w(5) == approx(0.06058693718652419, 0.0001)
