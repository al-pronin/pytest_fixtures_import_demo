Пример импорта фикстур 
из параллельного дерева директорий 
с помощью **pytest.plugins**

Фикстуры находятся в папке *fixtures*

Тесты - в папке *tests* на том же уровне

Запуск:

    git clone git@github.com:al-pronin/pytest_fixtures_import_demo.git
    cd pytest_fixtures_import_demo
    poetry shell
    poetry install
    poetry run pytest tests/test.py  