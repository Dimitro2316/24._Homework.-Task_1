from myapp.models import Book

# Вставка записей
Book.objects.bulk_create([
    Book(title='Война и мир', author='Лев Толстой', year=1869, price=500.00),
    Book(title='1984', author='Джордж Оруэлл', year=1949, price=300.00),
    Book(title='Мастер и Маргарита', author='Михаил Булгаков', year=1967, price=450.00),
    Book(title='Гарри Поттер и философский камень', author='Джоан Роулинг', year=1997, price=350.00),
    Book(title='Убить пересмешника', author='Харпер Ли', year=1960, price=400.00),
])

# Выбор всех записей, отсортированных по году издания
books_sorted_by_year = Book.objects.all().order_by('year')
for book in books_sorted_by_year:
    print(f"{book.title}, {book.year}")

# Выбор книг с ценой выше 400
expensive_books = Book.objects.filter(price__gt=400)
for book in expensive_books:
    print(f"{book.title}, {book.price}")

# Обновление цены книги с ID 1
Book.objects.filter(id=1).update(price=550.00)

# Удаление книг, у которых год издания меньше 1950
Book.objects.filter(year__lt=1950).delete()

