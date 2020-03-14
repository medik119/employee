from django import forms


from .models import Employee


class EmployForm(forms.ModelForm):
    positions = (
        (None,'Выберите должность сотрудника'),
        ('cook','Повар'),
        ('shift_chef','Повар смены'),
        ('foreman','Бригадир'),
        ('sous_chef','Су шеф'),
        ('chef','Шеф повар')
    )

    


    last_name = forms.CharField(label ='Фамилия',max_length = 50)
    first_name = forms.CharField(label ='Имя', max_length = 50)
    middle_name = forms.CharField(label ='Отчество',max_length = 50 )
    position = forms.ChoiceField( choices=positions)
    pay = forms.DecimalField(max_digits=7,decimal_places=0)

    class Meta:
        model = Employee
        fields =('last_name','first_name','middle_name','position','pay')


   
    
    
   




