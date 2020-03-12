from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import AbstractUser

class Employee(MPTTModel):
    positions = (
        (None,'Выберите должность сотрудника'),
        ('cook','Повар'),
        ('shift_chef','Повар смены'),
        ('foreman','Бригадир'),
        ('sous_chef','Су шеф'),
        ('chef','Шеф повар')
    )


    last_name = models.CharField(verbose_name ='Фамилия',max_length = 50)
    first_name = models.CharField(verbose_name ='Имя', max_length = 50)
    middle_name = models.CharField(verbose_name ='Отчество',max_length = 50 )
    position = models.CharField(verbose_name = 'Должность',choices=positions,max_length=50)
    employment_date  = models.DateField(verbose_name='Дата приема на работу', auto_now=True)
    pay = models.DecimalField(max_digits=7,decimal_places=0)
    parent = TreeForeignKey('self',on_delete = models.CASCADE,null = True,blank=True, related_name = 'children')

    class MPTTMeta:
        order_inversion_by = ['first_name']
    

    def __str__(self):
        return self.position 


    


