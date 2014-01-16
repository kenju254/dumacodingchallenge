dumacodingchallenge
===================

App built to assign users locations
----------------------------------


Simply clone this repository or you might as well fork it.

Create a Virtual Environment for it

Activate your Virtual Environmbent install the dependancies using
this command `pip freeze -r pathtorequirements.txt`

You will need to delete the current site.db that is on the repositoy and create another one

Sync the Database with this command `python manage.py syncdb` 

You will need to make the manage.py file executable by changine the permissions
with this `chmod a+x manage.py`

Next thing will be migrating the places app with 
`./manage.py migrate places`

There are a couple of CSV scripts that need to be loaded to your database. I simplified this with one script
`./manage.py load_data`

Now you can run the app with this
`./manage.py runserver`

I built this app for a challenge fill free to play around with fork it and make it better
