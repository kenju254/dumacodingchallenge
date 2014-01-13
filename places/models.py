from django.db import models



class County(models.Model):
    '''County Models'''
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255, default='',
                            blank=True)

    def __unicode__(self):
        return self.name



class Ward(models.Model):
    '''Ward Models'''
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255, default='',
                            blank=True)
    county = models.ForeignKey(County)

    def __unicode__(self):
        return self.name



class Location(models.Model):
    '''Location Models'''
    name = models.CharField(max_length=255)
    num = models.CharField(max_length=255, default='',
                            blank=True)
    latitude = models.CharField(max_length=255, default='0.000000',
                                 blank=True)

    longitude = models.CharField(max_length=255, default='0.000000',
                                blank=True)

    ward = models.ForeignKey(Ward)