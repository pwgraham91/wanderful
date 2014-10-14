from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from mapping.models import Traveler, Location, List
from django import forms


class TravelerUserCreationForm(UserCreationForm):

    class Meta:
        model = Traveler
        fields = ("username", "first_name", "last_name", "password1", "password2", "email")
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Traveler.objects.get(username=username)
        except Traveler.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

class LocationForm(forms.Form):
    city = forms.CharField()

class ListForm(ModelForm):
    class Meta:
        model = List
