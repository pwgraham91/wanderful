from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from mapping.forms import TravelerUserCreationForm, LocationForm, ListForm
from models import Location, Traveler, List


def home(request):
    locations = Location.objects.all()
    data = {
        'locations': locations,
    }
    return render(request, 'home.html', data)


def register(request):
    if request.method == 'POST':
        form = TravelerUserCreationForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/")
    else:
        form = TravelerUserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required()
def profile(request):
    lists = List.objects.filter(user__username=request.user)
    form = ListForm(request.POST)
    locations = Location.objects.all()

    if request.method == "POST":
        if form.is_valid():
            if form.save():
                data = {
                    'traveler': request.user,
                    'lists': lists,
                    'form': form,
                    'locations': locations,
                }
                return render(request, 'profile.html', data)
    data = {
        'traveler': request.user,
        'lists': lists,
        'form': form,
        'locations': locations,
    }
    return render(request, 'profile.html', data)


def location_form(request):
    locations = Location.objects.all()
    data = {"location_form": LocationForm()}
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            Location.objects.create(city_state=form.cleaned_data['city_state'])
            data = {"location_form": form, "locations": locations}
            return render(request, "home.html", data)

    else:
        return render(request, "location_form.html", data)