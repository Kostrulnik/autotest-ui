import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURES] Удаляем все данные из бд")


@pytest.fixture
def fill_books_database():
    print("[FIXTURES] Создаем новые данные из бд")


@pytest.mark.usefixtures("fill_books_database")
def test_read_all_books_in_library():
    print("Reading all books")


@pytest.mark.usefixtures(
    "clear_books_database",
    "fill_books_database",
)
class TestLibrary:
    def test_read_books_from_library(self):
        ...

    def test_delete_books_from_library(self):
        ...
