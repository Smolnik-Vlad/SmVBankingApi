from django.db.models.signals import post_delete
from django.dispatch import receiver

from users.models import Client, Employee


@receiver(post_delete, sender=Client)
def delete_customer(sender, instance, **kwargs):
    instance.user.delete()


@receiver(post_delete, sender=Employee)
def delete_customer(sender, instance, **kwargs):
    instance.user.delete()
