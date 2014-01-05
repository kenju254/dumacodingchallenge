from django.db import models


'''County Models'''
class County(models.Model):
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255, default='',
                            blank=True)

    def __unicode__(self):
        return self.name


'''Ward Models'''
class Ward(models.Model):
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255, default='',
                            blank=True)
    county = models.ForeignKey(County)

    def __unicode__(self):
        return self.name


'''Location Models'''
class Location(models.Model):
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255, default='',
                            blank=True)
    latitude = models.CharField(max_length=255, default='0.000000',
                                 blank=True)

    longitude = models.CharField(max_length=255, default='0.000000',
                                blank=True)

    ward = models.ForeignKey(Ward)