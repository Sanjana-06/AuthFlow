from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_welcome_email

@receiver(post_save, sender=User)
def send_email_on_registration(sender, instance, created, **kwargs):
    if created and instance.email:
        send_welcome_email.delay(instance.email)
