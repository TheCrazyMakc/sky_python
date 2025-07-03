import pytest
from string_utils import StringUtils

# Создаем экземпляр класса для тестов
utils = StringUtils()

# Тесты для метода capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("PYTHON", "Python"),
    ("", ""),
    ("test String", "Test string")
])
def test_capitalize(input_str, expected):
    result = utils.capitalize(input_str)
    assert result == expected

# Тесты для метода trim
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("    hello", "hello"),
    ("   ", ""),
    ("no spaces", "no spaces"),
    ("  leading and trailing  ", "leading and trailing  ")
])
def test_trim(input_str, expected):
    result = utils.trim(input_str)
    assert result == expected

# Тесты для метода contains
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("test", "t", True),
    ("test", "z", False),
    ("", "a", False),
    ("a", "a", True)
])
def test_contains(input_str, symbol, expected):
    result = utils.contains(input_str, symbol)
    assert result == expected

# Тесты для метода delete_symbol
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaaa", "a", ""),
    ("test test", "t", "es es"),
    ("no delete", "z", "no delete"),
    ("", "a", "")
])
def test_delete_symbol(input_str, symbol, expected):
    result = utils.delete_symbol(input_str, symbol)
    assert result == expected
