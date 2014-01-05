#! usr/bin/env/ python

import os
import sys
import csv

from django.core.management import setup_environ
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'Duma')))
from Duma import settings
setup_environ(settings)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from places.models import County, Ward, Location

county_data = open(os.path.join(os.path.dirname(__file__),'csvdata','userdata_county.csv' ))
ward_data = open(os.path.join(os.path.dirname(__file__), 'csvdata', 'userdata_ward.csv'))
location_data = open(os.path.join(os.path.dirname(__file__), 'csvdata', 'userdata_location.csv'))

'''Loading Counties into the Database'''
def insert_counties():
    with county_data:
        reader = csv.DictReader(county_data, fieldnames=['name','num'])
        for row in reader:
            county = County(name=row['name'],
                            num=row['num'])
            county.save()


'''Loading Wards into the Database'''
def insert_wards():
    with ward_data:
        reader = csv.DictReader(ward_data, fieldnames=['num','name', 'countynum'])
        for row in reader:
            ward = Ward(name=row['name'],
                        num=row['num'])

        #Try catch block connects the countynum to the ward table
            try:
                ward.county = County.objects.get(num=row['countynum'])
            except:
                pass
            else:
                ward.save


'''Loading Locations into the Database'''
def insert_locations():
    with location_data:
        reader = csv.DictReader(location_data, fieldnames=['num','name','wardnum', 'countynum','latitude','longitude'])
        for row in reader:
            location = Location(name=row['name'],
                                num=row['num'],
                                latitude=row['latitude'],
                                longitude=row['longitude'])
            try:
                location.ward = Ward.objects.get(num=row['wardnum'])
            except:
                pass
            else:
                location.save()


