from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(models.Model):
    username = models.CharField(max_length=150)

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f'Signal executed for user: {instance.username}')

# Simulating user creation within a transaction
try:
    with transaction.atomic():
        user = User(username='transaction_user')
        user.save()  # Signal will run within this transaction
        raise Exception('Simulating a transaction failure')
except Exception as e:
    print(f'Transaction rolled back: {e}')
