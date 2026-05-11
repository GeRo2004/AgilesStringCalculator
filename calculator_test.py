import pytest as pytest
from calculator import calculator

def test_string_vacio_devuelve_0():
    assert calculator.calculator("") == 0