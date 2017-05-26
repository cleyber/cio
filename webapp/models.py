from django.db import models

class User(models.Model):
    db_table = 'users'

    ROLE = (
        ('AD', 'Admin')
        ('EM', 'Employee')
    )
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=2, choices=ROLE, default='EM')

class Schedule(models.Model):
    db_table = 'schedules'

    date = models.DateField()
    start = models.DateTimeField()
    finish = models.DateTimeField()
    userId = model.ForeignKey(User, on_delete=models.CASCADE)

class Paysheet(models.Model):
    db_table = 'paysheet'

    total = models.DecimalField()
    start = models.DateTimeField()
    finish = models.DateTimeField()

class Configuration(models.Model):
    db_table = 'configurations'

    price = models.DecimalField()
    userId = model.ForeignKey(User, on_delete=models.CASCADE)
