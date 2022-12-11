from datetime import datetime

from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30, verbose_name='name')
    birth_date = models.DateField(verbose_name='Birth Date')

    def get_age(self):
        return f'{self.name}-{datetime.today().year - self.birth_date.year}'

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Employee(AbstractPerson):
    position = models.CharField(max_length=60)
    salary = models.CharField(max_length=60)
    work_experience = models.DateTimeField(verbose_name='Work Experience')

    def __str__(self):
        return f'{self.name}-{self.salary}-{self.position}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return print(f'{self.name} в должности {self.position} успешно сохранен!')


class Passport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='passports')
    INN = models.CharField(max_length=14, verbose_name='INN')
    id_card = models.IntegerField(verbose_name='ID card')

    def __str__(self):
        return f'{self.employee.name} ID:{self.id_card}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return print(f'{self.employee} с паспортом {self.id_card} успешно сохранен!')

    def get_gender(self):
        if self.INN[0] == '1':
            return 'Woman'
        elif self.INN[0] == '2':
            return 'man'
        else:
            'gay'


class WorkProject(models.Model):
    employee = models.ManyToManyField(Employee, related_name='employees', through='Membership')
    project_name = models.CharField(max_length=30, verbose_name='Project name')

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return print(f'{self.employee} учасвтующие в {self.project_name} успешно сохранены!')


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField(verbose_name='Date joined')

    def __str__(self):
        return self.employee

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return f'{self.employee} в проекте {self.work_project} успешно сохранен'


class Client(AbstractPerson):
    address = models.CharField(max_length=100, verbose_name='Address')
    phone_number = models.CharField(max_length=13, verbose_name='Phone Number')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return f'клиент {self.name}успешно сохранен'


class VIPClient(Client):
    vip_status_start = models.DateTimeField(verbose_name='VIP')
    donation_amount = models.IntegerField(verbose_name='Donation Amount')

    def __str__(self):
        return f'{self.name} VIP'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return f'{self.name} c донатом в {self.donation_amount} успешно сохранен'
