from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User  # Ensure this import is correct

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f'User {instance.username} saved.')
