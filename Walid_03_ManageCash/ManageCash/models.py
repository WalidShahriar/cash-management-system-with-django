from django.db import models
from django.contrib.auth.models import AbstractUser



class customUser(AbstractUser):

    pass
    def __str__(self):
        return f'{self.username}'

class AddCash(models.Model):

    user = models.ForeignKey(
        customUser,
        on_delete=models.SET_NULL,
        null=True
    )
    source = models.CharField(null=True, max_length=100)
    datetime = models.DateField(auto_now_add=True)
    amount = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username}'

class Expense(models.Model):

    user = models.ForeignKey(
        customUser,
        on_delete=models.SET_NULL,
        null=True
    )
    datetime = models.DateField(auto_now_add=True)
    amount = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username}'