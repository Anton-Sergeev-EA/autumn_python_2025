# todo: Заданы множества.
# Даны читатели книг.
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1'}
#Даны читатели газет.
readers_magazines = {'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
# Находим пересечение множеств (читатели, которые есть в обоих множествах).

common_readers = readers_books.intersection(readers_magazines)
# Вариант с &: common_readers = readers_books & readers_magazines

print("Пользователи, которые читают и книги, и газеты:")
print(common_readers)




