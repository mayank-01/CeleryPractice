from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celerytut import settings

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "Sample test mail to test celery project\nThank You"
        to_mail = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_mail],
            fail_silently=True
        )
    return "Done" 