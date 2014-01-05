from django.db import models
from django.contrib.auth.models import User

'''User Profile '''
class Profile(models.Model):
    phone_number = models.CharField(max_length=255)
    user = models.OneToOneField(User)

    #returns the first name and the phone number
    def __unicode__(self):
        return self.user.first_name + " " +  self.phone_number