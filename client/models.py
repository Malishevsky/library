from django.db import models

class LibraryClient(models.Model):
    family_name = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    middle_name = models.CharField(max_length=255,verbose_name='Отчество', null=True, blank=True)
    passport_number = models.CharField(max_length=255,verbose_name='Номер паспорта', unique=True, null=True, blank=True)
    date_of_bitrh = models.DateField(verbose_name='Дата рождения')
    e_mail = models.EmailField(unique=True, verbose_name='Адрес электроной почты')

    def __str__(self):
        return f'{self.family_name} {self.name}'
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class ClientAdress(models.Model):
    client = models.OneToOneField(to='LibraryClient',verbose_name='Клиент',on_delete=models.CASCADE)
    country = models.CharField(max_length=255, verbose_name='Cтрана', null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name='Город', null=True, blank=True)
    street = models.CharField(max_length=255, verbose_name='Город', null=True, blank=True)
    home_number = models.PositiveIntegerField(verbose_name='Номер дома', null=True, blank=True)
    apartment_number = models.PositiveIntegerField(verbose_name='Номер квартиры', null=True, blank=True)


    def __str__(self):
        return f'Адрес {self.client.name}'
    
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

class OwnedBook(models.Model):
    client = models.ForeignKey(to='LibraryClient',verbose_name='Клиент',on_delete=models.CASCADE)
    owneded_book = models.ForeignKey(to='main.Book',verbose_name='Книга',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.owneded_book.russian_name} {self.client.name}'
    
    class Meta:
        verbose_name = 'Выданная книга'
        verbose_name_plural = 'Выданные книги'