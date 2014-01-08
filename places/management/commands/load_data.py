#! usr/bin/env/ python

import os
import sys
import csv

#from django.core.management import setup_environ
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Duma')))
#from Duma import settings
#setup_environ(settings)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.management.base import BaseCommand
from places.models import County, Ward, Location

county_data = open(os.path.join(os.path.dirname(__file__),'csvdata','userdata_county.csv' ))
ward_data = open(os.path.join(os.path.dirname(__file__), 'csvdata', 'userdata_ward.csv'))
location_data = open(os.path.join(os.path.dirname(__file__), 'csvdata', 'userdata_location.csv'))

class Command(BaseCommand):

    def insert_counties(self):
        ''' Loading Counties into the Database'''
        with county_data:
            self.reader = csv.DictReader(county_data, fieldnames=['name','num'])
            for row in self.reader:
                self.county = County(name=row['name'],
                    num=row['num'])
                self.county.save()



    def insert_wards(self):
        '''Loading Wards into the Database'''
        with ward_data:
            self.reader = csv.DictReader(ward_data, fieldnames=['num','name', 'countynum'])
            for row in self.reader:
                self.ward = Ward(name=row['name'],
                    num=row['num'])

                #Try catch block connects the countynum to the ward table
                try:
                    self.ward.county = County.objects.get(num=row['countynum'])
                except:
                    pass
                else:
                    self.ward.save()



    def insert_locations(self):
        '''Loading Locations into the Database'''
        with location_data:
            self.reader = csv.DictReader(location_data, fieldnames=['num','name','wardnum', 'countynum','latitude','longitude'])
            for row in self.reader:
                self.location = Location(name=row['name'],
                                        num=row['num'],
                                        latitude=row['latitude'],
                                        longitude=row['longitude'])
                try:
                    self.location.ward = Ward.objects.get(num=row['wardnum'])
                except:
                    pass
                else:
                    self.location.save()





    def handle(self, *args, **options):
        self.insert_counties()
        self.insert_wards()
        self.insert_locations()



