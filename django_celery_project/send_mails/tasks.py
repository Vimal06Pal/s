from django.contrib.auth import get_user_model
from celery import shared_task

@shared_task(bind=True)
def send_mail_func(self):
    #operations
    users  =get_user_model().objects.all()
    for user in users:
        

    return('Done')