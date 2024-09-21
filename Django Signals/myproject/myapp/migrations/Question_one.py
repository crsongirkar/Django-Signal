from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(models.Model):
    username = models.CharField(max_length=150)

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f'Signal executed for user: {instance.username}')

# Simulating user creation
user = User(username='testuser')
user.save()  # This will trigger the signal synchronously
