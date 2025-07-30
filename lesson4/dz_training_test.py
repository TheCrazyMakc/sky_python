import pytest
from dz_training import StringProcessor

# Позитивные тесты
def test_process_normal_string():
    # Тест с обычной строкой без точки
    result = StringProcessor.process("hello world")
    assert result == "Hello world."

def test_process_string_with_dot():
    # Тест со строкой, уже заканчивающейся точкой
    result = StringProcessor.process("Hello world.")
    assert result == "Hello world."

def test_process_single_word():
    # Тест с одним словом
    result = StringProcessor.process("test")
    assert result == "Test."

def test_process_empty_string():
    # Тест с пустой строкой
    result = StringProcessor.process("")
    assert result == "."

def test_process_string_with_leading_whitespace():
    # Тест со строкой, содержащей пробелы в начале
    result = StringProcessor.process("   example")
    assert result == "   example."

# Негативные тесты
def test_process_none():
    # Тест с None вместо строки
    result = StringProcessor.process(None)
    assert result == "."  # Ожидаем точку, так как метод возвращает "." для пустого ввода


def test_process_non_string():
    # Тест с нестроковым значением
    with pytest.raises(TypeError):
        StringProcessor.process(12345)
