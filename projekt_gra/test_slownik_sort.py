from slownik_sort import sorted_slownik
import pytest

def test_sorted_slownik():
    slownik = {'a' : 2, 'csacsa' : 1, 'iop' : 10, 'posad' : 4}
    assert sorted_slownik(slownik) == {'iop' : 10, 'posad' : 4, 'a' : 2, 'csacsa' : 1}