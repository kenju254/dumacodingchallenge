from django.conf.urls import patterns, include, url
#from main.views import select_user, select_location, show_result

urlpatterns = patterns('',
    url('^$', 'main.views.select_user'),
    url('^location/$', 'main.views.select_location'),
    url('^success/$', 'main.views.show_result'),


)