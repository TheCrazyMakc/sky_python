import pytest
empty_dict = {}

def test_read_dict():
    with pytest.raises(KeyError):
      empty_dict["key"]

def test_get_empty():
  value = empty_dict.get("key")
  assert value == None


def test_empty_dict():
  assert len(empty_dict) == 0

football_stats = {
    "Число стран": 48,
    "Страна": "Катар",
    "Участники": ["Австралия", "Англия", "Аргентина", "Бельгия", "еще 42 страны", "Эквадор", "Япония"],
    "Награды": {
        "Золотой мяч": "Лионель Месси",
        "Серебряный мяч": "Килиан Мбаппе",
        "Золотая бутса": "Килиан Мбаппе",
        "Серебряная бутса": "Килиан Мбаппе",
        "Золотой мяч": "Лионель Месси",
        "Больше всего голов": {
            "Игрок": "Килиан Мбаппе - капитан команды",
            "Количество мячей": 8
        }
    }
}

def test_read_value():
    count = football_stats.get("Число стран")
    assert count == 48

def test_read_value_country():
    country = football_stats["Страна"]
    assert country == "Катар"

def test_write_value():
    football_stats["Число стран"] = 50
    count = football_stats.get("Число стран")
    assert count == 50

