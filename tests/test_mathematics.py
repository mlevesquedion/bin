from pytest import mark
from mathematics import floor_root, is_prime


@mark.parametrize(
    ('n', 'expected'),
    (
        *[(n, int(n**0.5)) for n in range(2, 11)],
        (123456789, 11111),
    )
)
def test_floor_root(n, expected):
    assert expected == floor_root(n)


@mark.parametrize(
    ('n', 'expected'),
    (
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (37, True),
        (912347928593, True),
        (912347928594, False),
    )
)
def test_is_prime(n, expected):
    assert expected == is_prime(n)
