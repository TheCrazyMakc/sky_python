import pytest
from string_utils import StringUtils

# Создаем экземпляр класса для тестов
utils = StringUtils()

# Тесты для метода capitalize ПОЗИТИВНЫЕ проверки
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("PYTHON", "Python"),
    ("test String", "Test string")
])
def test_capitalize_positive(input_str, expected):
    result = utils.capitalize(input_str)
    assert result == expected

# Тесты для метода capitalize НЕГАТИВНЫЕ проверки
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),    # Числа в начале
    ("", ""),
    ("!hello", "!hello"),    # Символы препинания
])
def test_capitalize_negative(input_str, expected):
    result = utils.capitalize(input_str)
    assert result == expected

# Тесты для метода trim ПОЗИТИВНЫЕ проверки
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("    hello", "hello"),
    ("   ", ""),
    ("no spaces", "no spaces"),
    ("  leading and trailing  ", "leading and trailing  ")
])
def test_trim_positive(input_str, expected):
    result = utils.trim(input_str)
    assert result == expected

# Тесты для метода trim НЕГАТИВНЫЕ проверки
@pytest.mark.parametrize("input_str, expected", [
    ("   123", "123"),
    ("    !!!hello", "!!!hello"),
])
def test_trim_negative(input_str, expected):
    result = utils.trim(input_str)
    assert result == expected

# Тесты для метода contains ПОЗИТИВНЫЕ проверки
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("test", "t", True),
    ("test", "z", False),
    ("", "a", False),
    ("a", "a", True)
])
def test_contains_positive(input_str, symbol, expected):
    result = utils.contains(input_str, symbol)
    assert result == expected

# Тесты для метода contains НЕГАТИВНЫЕ проверки
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro!", "!", True),
    ("SkyPro3", "3", True),
    ("123", "5", False),
    ("123", "2", True),
])
def test_contains_negative(input_str, symbol, expected):
    result = utils.contains(input_str, symbol)
    assert result == expected

# Тесты для метода delete_symbol ПОЗИТИВНЫЕ проверки
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaaa", "a", ""),
    ("test test", "t", "es es"),
    ("no delete", "z", "no delete"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    result = utils.delete_symbol(input_str, symbol)
    assert result == expected

# Тесты для метода delete_symbol НЕГАТИВНЫЕ проверки
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("12345", "3", "1245"),
    ("test\nline", "\n", "testline"),
    ("", "a", "")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    result = utils.delete_symbol(input_str, symbol)
    assert result == expected