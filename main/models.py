from django.db import models
from django.core.mail import send_mail

from places.models import Location, Ward
from userprofile.models import Profile
from Duma.settings import EMAIL_RECEPIENT

class MappingManager(models.Manager):
    def add_new_location(self , name, profile):
        matches = Location.objects.filter(name__iexact=name)
        if matches:
            location = matches[0]
        else:
            location = Location(name=name,
                                ward=Ward.objects.get(name__iexact='other'))
            location.save()
            user_name = "%s %s" %(profile.user.first_name, profile.user.last_name)
            subject = 'User adds new location'
            body = "Dear Eric, a user by the name %s has added a new location by the name '%s'."  %(user_name, name)
            fromme = 'noreply@localhost'
            to =   EMAIL_RECEPIENT
            send_mail(subject, body, fromme, [to, 'kenmbugua@gmail.com'], fail_silently=False)

        mapping = Mapping(
            profile=profile,
            location=location)
        mapping.save()
        return mapping

class Mapping(models.Model):
    profile = models.ForeignKey(Profile)
    location = models.ForeignKey(Location)
    objects = MappingManager()

    def __unicode__(self):
        return self.profile.user.first_name + '-' + self.location.name







