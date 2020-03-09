from employee.models import Employee
from random import choice

first_name_list = 'Мухаммед Денис Роман Александр Сергей Дмитри Алексей Прокофий Дмитрий Андрей Матвей Петр Евгений'.split()

last_name_list = 'Курайши Комаров Михалков Ногиев Денисов Селязнёв Лябушев Мамышев Кутлова Богомирская'.split()

middle_name_list ='Русланович Денисович Владимирович Анатольевич Абасович Валерьевич Мухамедович Игнатьевич'.split()



def main():
    for i in range(1,3):
        Employee.objects.create(first_name = choice(first_name_list),last_name = choice(last_name_list),middle_name = choice(middle_name_list),
        position = 'chef',pay = 150000,parent=None)
    
    chef_list  = Employee.objects.filter(position = 'chef')
    for i in chef_list:
        for y in range(1,3):
            Employee.objects.create(first_name = choice(first_name_list),last_name = choice(last_name_list),middle_name = choice(middle_name_list),
            position = 'sous_chef',pay = 100000,parent=i)
    
    sous_chef_list = Employee.objects.filter(position = 'sous_chef')
    for i in sous_chef_list:
        for y in range(1,5):
            Employee.objects.create(first_name = choice(first_name_list),last_name = choice(last_name_list),middle_name = choice(middle_name_list),
            position = 'foreman',pay = 800000,parent=i)

    foreman_list = Employee.objects.filter(position = 'foreman')

    for i in foreman_list:
        for y in range(1,8):
            Employee.objects.create(first_name = choice(first_name_list),last_name = choice(last_name_list),middle_name = choice(middle_name_list),
            position = 'shift_chef',pay = 75000,parent=i)
    
    shift_chef =Employee.objects.filter(position = 'shift_chef')

    for i in shift_chef:
        for y in range(1,19):
            Employee.objects.create(first_name = choice(first_name_list),last_name = choice(last_name_list),middle_name = choice(middle_name_list),
            position = 'cook',pay = 50000,parent=i)
    



    



   
    
    





if __name__ == "__main__":
    main()




