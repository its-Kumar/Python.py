import pytest

import mathlib


# skipping test
@pytest.mark.skip(reason="I don't want to run the test right now")
def test_calc_total():
    total = mathlib.calc_total(4, 5)
    assert total == 9


def test_calc_mul():
    result = mathlib.calc_mul(10, 3)
    assert result == 30


@pytest.mark.parametrize(
    "test_input, expected_output", [(5, 25), (9, 81), (10, 100), (-2, 4)]
)
def test_calc_sqaure(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output


"""
Running test:

`python -m pytest`
`py.test`
`py.test -v`
`py.test -v -rxs`
`py.test -k mul` # run only the test which has 'mul' in its name
"""
