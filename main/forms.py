from django import forms

from userprofile.models import Profile
from places.models import County, Ward, Location

# User Variable fetches all the user data from the Database
users = ((profile.pk, "%s %s, %s" %(profile.user.first_name, profile.user.last_name, profile.phone_number))
        for profile in Profile.objects.all())

#Counties Variable fetches all the county data from the Database
counties = ((county.pk,"%s" % county.name)
            for county in County.objects.all())

class BaseForm(forms.Form):
    """The Base Form that has the others field"""
    others = forms.CharField(required=False)

class CountyForm(BaseForm):
    """ The CountyForm that handles the user selection of Counties """
    county = forms.ChoiceField(choices=counties, required=False)

class UsersForm(BaseForm):
    """The UserForm that enables the users to fill in their information """
    user = forms.ChoiceField(choices=users, required=True)


def get_ward_form(county):
    """Function that gets the ward form"""

    #ward variable fetches all the ward data from the Database
    wards = ((ward.pk,"%s , %s"%(ward.name, ward.county.name))
            for ward in Ward.objects.filter(county=county))

    class WardForm(BaseForm):
        """The Ward Form enables the users to fill in the ward data"""
        ward = forms.ChoiceField(choices=wards,required=False)

    return WardForm

def get_location_form(ward):
    locations = ((location.pk, "%s, %s" %(location.name, location.ward.county.name))
                for location in Location.objects.filter(ward=ward))

    class LocationForm(BaseForm):
        location = forms.ChoiceField(choices=locations, required=False)

        def clean(self):
            cleaned_data = super(LocationForm, self).clean()
            location = cleaned_data.get('location')
            other = cleaned_data.get('other')
            print location; print other; print cleaned_data

            if location and other:
                location = Location.objects.get(pk=int(location)).name
                raise forms.ValidationError("Please select only one location"
                                            "You can't have both '%s' and '%s' " %(location, other))

            return cleaned_data

    return LocationForm








