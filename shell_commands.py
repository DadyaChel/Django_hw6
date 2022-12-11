from employee.models import *
from django.db.models import Q, Subquery

emp1 = Employee.objects.create(
    name='Asy',
    birth_date='1889-04-20',
    position='dictator',
    salary=470000,
    work_experience='1919-11-02'
)
emp2 = Employee.objects.create(
    name='Dadya',
    birth_date='2004-05-02',
    position='NN',
    salary=000000,
    work_experience='2004-05-02'
)
emp3 = Employee.objects.create(
    name='Papizy',
    birth_date='1990-11-19',
    position='strimer',
    salary=999999999999999,
    work_experience='2015-12-12'
)
emp4 = Employee.objects.create(
    name='Doter',
    birth_date='2021-10-10',
    position='ADun',
    salary=0,
    work_experience='1000-01-01'
)
inn1 = Passport.objects.create(name=emp1, INN='22004188999999', id_card=29792)
inn2 = Passport.objects.create(name=emp2, INN='10205200499999', id_card=29792)
inn3 = Passport.objects.create(name=emp3, INN='21911199099999', id_card=29792)
inn4 = Passport.objects.create(name=emp4, INN='61010202199999', id_card=29792)

emp_del = Employee.objects.all().order_by('-name')
emp_del[0].delete()


name1 = Employee.objects.all()[0]
name2 = Employee.objects.all()[1]
name3 = Employee.objects.all()[2]

emp6 = Employee.objects.create(
    name='Asy',
    birth_date='1889-04-20',
    position='dictator',
    salary=470000,
    work_experience='1919-11-02'
)

wp = WorkProject.objects.create(project_name='3m')
wp1 = WorkProject.objects.create(project_name='kakoito project')
wp1.employee.set([emp6, name2])

wp_delete = Membership.objects.all()[2]
wp_delete.delete()


emp5 = Employee.objects.create(name='Loki', birth_date='1887-22-11', position='vor',
                               salary=12345, work_experience='2012-12-04')

wp_1 = WorkProject.objects.all()[0]
wp_1.employee.set([emp5])


client1 = Client.objects.create(name='Tor', birth_date='2001-02-14', address='Asgard')
client2 = Client.objects.create(name='Sasha', birth_date='1999-07-07', address='GrayLand')
client3 = Client.objects.create(name='Chort', birth_date='2012-05-09', address='Ratusha')


vip_person = VIPClient.objects.create(name='Gattsu', birth_date='1700-06-12',
                                      address='ylitsa', phone_number='+900567303890', vip_status_start='1700-06-12',
                                      donation_amount=777777777777)
# cli_delete = Client.objects.all()[0]
# cli_delete.delete()

print(f'все сотрудники-{Employee.objects.all()}')
employee_with_id = Passport.objects.filter(
    Q(id_card__contains='1') |
    Q(id_card__contains='2') |
    Q(id_card__contains='3') |
    Q(id_card__contains='4') |
    Q(id_card__contains='5') |
    Q(id_card__contains='6') |
    Q(id_card__contains='7') |
    Q(id_card__contains='8') |
    Q(id_card__contains='9') |
    Q(id_card__contains='0')
)
print(f'сотрудники с паспортом{employee_with_id}')
print(f'проекты{WorkProject.objects.all()}')
print(f"проекты в которых участвую я{WorkProject.objects.filter(participants__name__startswith='Dadya')}")
print(f'клиенты{Client.objects.all()}')
print(f'VIP клиенты-{VIPClient.objects.all()}')

employee_1 = Passport.objects.all()[2]
print(Passport.get_gender(employee_1))

name = Employee.objects.all().first()
print(Employee.get_age(name))
