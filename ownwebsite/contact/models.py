from django.db import models


# Create your models here.
class Msg(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=50)
    msg_subject = models.CharField(max_length=50)
    msg_text = models.CharField(max_length=200)

    def __str__(self):
        return self.user_email+' : '+self.msg_subject
