Реализованные тесты:
test_add_new_book_and_default_rating -- Проверка добавления книг.
test_add_new_book_not_add_twice -- Нельзя добавить одну и ту же книгу дважды.
test_add_book_in_favorites -- Нельзя выставить рейтинг книге, которой нет в списке.
test_get_books_rating_book_not_list_not_rating -- У не добавленной книги нет рейтинга.
test_get_books_rating_not_add_less_one -- Нельзя выставить рейтинг меньше 1.
test_get_books_rating_not_add_more_ten -- Нельзя выставить рейтинг больше 10.
add_book_in_favorites_not_add_book_not_in_books_rating --Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
add_book_in_favorites -- Добавление книги в избранное.
delete_book_from_favorite -- Проверка удаления книги из избранного.