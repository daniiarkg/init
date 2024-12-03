from django.utils import timezone
from django.db import models
from random import choice

TYPE_CHOICES = [('1','Цветок'),('2', 'Кактус'),('3','Корнеплод'),]
STATUS_CHOICES = [('1','Стабильно'),('2','Требуется осмотр'),('3','Критическое')]

# Create your models here.
class Plant(models.Model):

    def __str__(self) -> str:
        return f'{str(self.id)} | {self.name}' 

    name = models.CharField(verbose_name='Наименование', max_length=200, null=True)
    type = models.CharField(verbose_name='Тип', max_length=1, null=True, choices=TYPE_CHOICES)
    photo = models.ImageField(verbose_name='Первичное фото', blank=True, upload_to='main')

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'


class Report(models.Model):

    def __str__(self) -> str:
        return f'{str(self.id)} | { str( self.date.strftime("%c") ) }'

    plant = models.ForeignKey(Plant, verbose_name='Растение', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(verbose_name='Дата', null=True, default=timezone.now)
    status = models.CharField(verbose_name='Статус', blank=True, max_length=1, choices=STATUS_CHOICES)
    photo = models.ImageField(verbose_name='Фото', upload_to='main', null=True)

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'