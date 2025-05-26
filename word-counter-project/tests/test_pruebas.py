import pytest
from src.pruebas import sumar

def test_sumar_enteros():
    assert sumar(2, 3) == 5

def test_sumar_flotantes():
    assert sumar(2.5, 3.5) == 6.0

def test_sumar_entero_y_flotante():
    assert sumar(2, 3.5) == 5.5

def test_sumar_negativos():
    assert sumar(-2, -3) == -5

def test_sumar_cero():
    assert sumar(0, 0) == 0