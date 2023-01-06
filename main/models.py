from django.db import models

class Book(models.Model):
    russian_name = models.CharField(verbose_name='Русское название книги',max_length=255)
    original_name = models.CharField(verbose_name='Оригинальное название книги',max_length=255,blank=True,null=True)
    genre = models.ManyToManyField(to='Genre',verbose_name='Жанр')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    book_count = models.PositiveIntegerField(verbose_name='Количество экземпляров')
    authors = models.ManyToManyField(to='Authors',verbose_name='Авторы')
    cover_img = models.FileField(upload_to=f'media/book/%Y/%m/%d/')
    one_use_day_price = models.PositiveBigIntegerField(verbose_name='Цена за 1 день')
    make_year = models.PositiveIntegerField(verbose_name='Год создания',null=True,blank=True)
    registration_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата регистрации')
    page_count = models.IntegerField(verbose_name='Количество страниц',null=True,blank=True)

    def __str__(self):
        return self.russian_name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-russian_name']


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр',max_length=150)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Authors(models.Model):
    name = models.CharField(verbose_name='Автор',max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    
class BookAuthorsFoto(models.Model):
    author = models.ForeignKey(to='Authors',verbose_name='Автор',on_delete=models.DO_NOTHING)
    autors_img = models.FileField(upload_to=f'media/author/%Y/%m/%d/',verbose_name='Фото автора',null=True,blank=True)
    main_book = models.ForeignKey(to='Book',verbose_name='Книга',on_delete=models.CASCADE)

    def __str__(self):
        return f'Фото {self.author.name}'

    class Meta:
        verbose_name = 'Фото автора'
        verbose_name_plural = 'Фото атворов'