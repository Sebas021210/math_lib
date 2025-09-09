import pytest
from mathlib.mathlib import square, factorial, is_prime, gcd, lcm

# ---- square ----
def test_square_positive():
    assert square(3) == 9

def test_square_negative():
    assert square(-4) == 16

def test_square_non_numeric_raises():
    with pytest.raises(TypeError):
        square("a")

# ---- factorial ----
def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_five():
    assert factorial(5) == 120

def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_non_int_raises():
    with pytest.raises(TypeError):
        factorial(3.5)

# ---- is_prime ----
def test_is_prime_two_and_large_prime():
    assert is_prime(2) is True
    assert is_prime(97) is True

def test_is_prime_zero_one():
    assert is_prime(0) is False
    assert is_prime(1) is False

def test_is_prime_non_int_raises():
    with pytest.raises(TypeError):
        is_prime(3.14)

# ---- gcd ----
def test_gcd_basic_and_negative():
    assert gcd(48, 18) == 6
    assert gcd(-4, 6) == 2

def test_gcd_with_zero():
    assert gcd(0, 5) == 5

def test_gcd_both_zero_raises():
    with pytest.raises(ValueError):
        gcd(0, 0)

# ---- lcm ----
def test_lcm_basic_and_negative():
    assert lcm(4, 6) == 12
    assert lcm(-3, 7) == 21

def test_lcm_with_zero():
    assert lcm(0, 5) == 0

def test_lcm_both_zero_raises():
    with pytest.raises(ValueError):
        lcm(0, 0)
