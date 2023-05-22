import pytest

from main import BooksCollector

name = 'Что делать, если ваш кот хочет вас убить'
other_name = 'Синдром петрушки'


class TestBooksCollector:
    def test_add_new_book_and_default_rating(self, books_collector):
        books_collector.add_new_book(name)

        assert books_collector.get_book_rating(name) == 1

    def test_add_new_book_not_add_twice(self, books_collector):
        books_collector.add_new_book(name)
        books_collector.add_new_book(name)

        assert len(books_collector.get_books_rating()) == 1, 'Error:not add book twice'

    def test_get_books_rating_book_not_list_not_rating(self, books_collector):
        name = 'Гарри Поттер и философский камень'

        assert books_collector.get_book_rating(name) is None

    def test_get_books_rating_not_add_less_one(self, books_collector):
        books_collector.add_new_book(name)
        books_collector.set_book_rating(name, 0)

        assert books_collector.get_book_rating(name) == 1

    def test_get_books_rating_not_add_more_ten(self, books_collector):
        books_collector.add_new_book(name)
        books_collector.set_book_rating(name, 15)

        assert books_collector.get_book_rating(name) == 1

    def test_get_books_rating_not_add_book_no_rating(self, books_collector):
        books_collector.add_new_book(name)
        books_collector.set_book_rating(other_name, 3)

        assert books_collector.get_book_rating(name) == 1

    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)

        assert name in books_collector.get_list_of_favorites_books()

    def test_delete_book_from_favorite(self, books_collector):
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)

        assert name not in books_collector.get_list_of_favorites_books()