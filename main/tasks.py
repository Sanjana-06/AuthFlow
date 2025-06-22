from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(username):
    send_mail(
        subject="Welcome to AuthFlow",
        message=f"Hi @{username}, thank you for registering with our Telegram bot!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[f"{username}@example.com"],  
    )
