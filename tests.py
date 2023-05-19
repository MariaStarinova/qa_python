import pytest

from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture(scope='function')
    def books_collector(self):
        return BooksCollector()

    name = 'Что делать, если ваш кот хочет вас убить'
    other_name = 'Синдром петрушки'

    def test_add_new_book_and_default_rating(self, books_collector):
        books_collector.add_new_book(self.name)

        assert books_collector.favorites == []
        assert books_collector.books_rating == {self.name: 1}


    def test_add_new_book_not_add_twice(self, books_collector):
        books_collector.add_new_book(self.name)
        books_collector.add_new_book(self.name)

        assert books_collector.favorites == []
        assert books_collector.books_rating == {self.name: 1}


    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_new_book(self.name)
        books_collector.add_book_in_favorites(self.name)

        assert self.name in books_collector.favorites


    def test_get_books_rating_book_not_list_not_rating(self, books_collector):
        name = 'Гарри Поттер и философский камень'
        rating = 10

        assert books_collector.books_rating.get(name) is None


    def test_get_books_rating_not_add_less_one(self, books_collector):
        books_collector.add_new_book(self.name)
        books_collector.set_book_rating(self.name, 0)

        assert books_collector.books_rating[self.name] == 1


    def test_get_books_rating_not_add_more_ten(self, books_collector):
        books_collector.add_new_book(self.name)
        books_collector.set_book_rating(self.name, 15)

        assert books_collector.books_rating[self.name] == 1


    def test_get_books_rating_not_add_book_no_rating(self, books_collector):
        books_collector.add_new_book(self.name)
        rating = books_collector.get_book_rating(self.other_name)

        assert rating is None


    def add_book_in_favorites(self, books_collector):
        books_collector.add_book_in_favorites(self.name)

        assert books_collector.favorites == []
        assert books_collector.books_rating == {}


    def delete_book_from_favorite(self, books_collector):
        books_collector.add_new_book(self.name)
        books_collector.add_book_in_favorites(self.name)
        books_collector.delete_book_from_favorites(self.name)

        assert books_collector.favorites == []
        assert books_collector.books_rating == {self.name: 1}



