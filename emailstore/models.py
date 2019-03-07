from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):
    email = models.CharField(max_length = 80)
    time_added = models.DateTimeField('date submitted')   
    
    def __str__(self):
        return self.email
