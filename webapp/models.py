from django.db import models

class User(models.Model):
    """docstring forUser."""
    db_table = 'users'

    ROLE = (
        ('ad', 'Admin')
        ('em', 'Employee')
    )
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=2, choices=ROLE)

class Schedule(models.Model):
    """docstring for Schedule"""
    db_table = 'schedules'

    date = models.DateField()
    start = models.DateTimeField()
    finish = models.DateTimeField()
    userId = model.ForeignKey(User, on_delete=models.CASCADE)

class Paysheet(models.Model)
    """docstring for Paysheet"""
    db_table = 'Paysheet'

    total = models.DecimalField()
    start = models.DateTimeField()
    finish = models.DateTimeField()
