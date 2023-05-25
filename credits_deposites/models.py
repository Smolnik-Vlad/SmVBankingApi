from django.db import models

from users.models import Client


# Create your models here.
class Credit(models.Model):
    user = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name='credits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Credit #{self.pk} - User: {self.user}"


class Deposit(models.Model):
    user = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name='deposits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Deposit #{self.pk} - User: {self.user}"
