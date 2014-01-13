from django.http import HttpResponse , HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

from userprofile.models import Profile
from places.models import County, Ward, Location


import forms
import models

def select_user(request, template_name='select_option.html'):
    if request.method == 'POST':
        form = forms.UsersForm(request.POST)
        if form.is_valid():
            profile_id = int(form.cleaned_data['user'])
            profile = get_object_or_404(Profile, pk=profile_id)
            request.session['user_profile'] = profile
            return HttpResponseRedirect(reverse(select_location))
    elif request.method == 'GET':
        form = forms.UsersForm()
    return render_to_response(template_name,
                            {'form': form},
                            context_instance=RequestContext(request))


def select_location(request, template_name='select_location.html'):
    label = ''
    if request.method == 'POST':
        if request.POST.get('other') and not request.POST.get('location'):
            form = forms.BaseForm(request.POST)
            mapping = models.Mapping.objects.add_location(name=form.cleaned_data['other'],
                                                        profile=request.session.get('user_profile'))
            request.session['mapping'] = mapping
            return HttpResponseRedirect(reverse(show_result))

        if request.POST.get('county'):
            form = forms.CountyForm(request.POST)
            if form.is_valid():
                county = get_object_or_404(County, pk=int(form.cleaned_data['county']))
                form = forms.get_ward_form(county)
                request.session['county'] = county.num
                label = 'ward'

        if request.POST.get('ward'):
            form = forms.get_ward_form(request.session['county'])
            form = form(request.POST)
            if form.is_valid():
                ward = get_object_or_404(Ward, pk=int(form.cleaned_data['ward']))
                form = forms.get_location_form(ward)
                request.session['ward']= ward.num
                label = 'location'

        if request.POST.get('location'):
            label = 'location'
            form = forms.get_location_form(request.session['ward'])
            form = form(request.POST); print request.POST
            if form.is_valid():
                location = get_object_or_404(Location,pk=int(form.cleaned_data['location']))
                mapping = models.Mapping(
                    profile=request.session['user_profile'],
                    location=location)
                mapping.save()
                request.session['mapping']= mapping
                request.session['county']= None
                request.session['ward']= None
                request.session['user_profile'] = None
                return HttpResponseRedirect(reverse(show_result))
    if request.method == 'GET':
        form = forms.CountyForm()
        label = 'county'


    return render_to_response(template_name,
                                {'form': form,
                                'label': label},
                                context_instance=RequestContext(request))


def show_result(request, template_name="show_result.html"):
    mapping = request.session.get('mapping')
    if mapping:
        name = "%s %S" % (mapping.profile.user.first_name,
                        mapping.profile.user.last_name)

        phone_number = mapping.profile.phone_number

        location = "%s %s" % (mapping.location.name,
                            mapping.location.ward.county.name)

        return render_to_response(template_name,
                                {'name':name,
                                 'phone_number': phone_number,
                                 'location': location,},
                                context_instance=RequestContext(request))










