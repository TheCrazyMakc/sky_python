class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной
        и возвращает этот же текст
        Пример: `capitilize("skypro") -> "Skypro"`
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        Пример: `trim("   skypro") -> "skypro"`
        """
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ
        и `False` - если нет
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ
        Пример 1: `contains("SkyPro", "S") -> True`
        Пример 2: `contains("SkyPro", "U") -> False`
        """
        res = False
        try:
            res = string.index(symbol) > -1  # Если символ найден, возвращается его индекс (число >= 0)
        except ValueError:
            pass

        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        Параметры:
            `string` - строка для обработки
            `symbol` - искомый символ для удаления
        Пример 1: `delete_symbol("SkyPro", "k") -> "SyPro"`
        Пример 2: `delete_symbol("SkyPro", "Pro") -> "Sky"`
        """
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string
    

utils = StringUtils()

print(StringUtils().capitalize("python"))    # Результат: "Python"
print(StringUtils().capitalize("TEST"))      # Результат: "Test"
print(StringUtils().capitalize(""))         # Результат: ""
print(StringUtils().capitalize(" test"))     # Результат: " Test"

print(StringUtils().trim("   skypro"))
print(StringUtils().trim("   "))
print(StringUtils().trim("no spaces"))
print(StringUtils().trim("  leading and trailing  "))


def test_contains(input_str, symbol, expected):
    result = utils.contains(input_str, symbol)
    print(f"Тестирование: строка='{input_str}', символ='{symbol}'")
    print(f"Ожидаемый результат: {expected}")
    print(f"Полученный результат: {result}")
    print(f"Тест {'пройден' if result == expected else 'не пройден'}\n")
    return result == expected

test_contains("SkyPro", "S", True)
test_contains("SkyPro", "U", False)
test_contains("test", "t", True)
test_contains("test", "z", False)
test_contains("", "a", False)
test_contains("a", "a", True)

print(StringUtils().delete_symbol("SkyPro", "k"))
print(StringUtils().delete_symbol("SkyPro", "Pro"))
print(StringUtils().delete_symbol("aaaa", "a"))
print(StringUtils().delete_symbol("test test", "t"))
print(StringUtils().delete_symbol("no delete", "z"))
print(StringUtils().delete_symbol("", "a"))