from django.db import models

from users.models import Client


# Create your models here.

class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts', db_index=True)
    account_number = models.CharField(max_length=50, unique=True, null=False, blank=False)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client.user}: {self.account_number}'

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Account'
        ordering = ['-balance', 'created_at']


class Transaction(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.SET_NULL, db_index=True, null=True,
                               related_name='sent_transactions')
    receiver = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='received_transactions')
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} ---> {self.receiver}'

    class Meta:
        verbose_name = 'Transactions'
        verbose_name_plural = 'Transaction'
        default_related_name = 'transactions'
