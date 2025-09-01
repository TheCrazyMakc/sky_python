Для запуска теста с Allure:

1. Установите allure-pytest:

bash > pip install allure-pytest

2. Запустите тест с генерацией отчетов:

bash > pytest --alluredir=allure-results your_test_file.py

3. Просмотрите отчет:

bash > allure serve allure-results