import pytest as pytest
from calculator import calculator

def test_string_vacio_devuelve_0():
     assert calculator.calculator("") == 0

def test_un_numero_devuelve_ese_numero():
    assert calculator.calculator("1") == 1

def test_dos_numeros_devuelve_suma():
    assert calculator.calculator("1,2") == 3