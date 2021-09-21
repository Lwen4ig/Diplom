import datetime
import requests
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.datetime_safe import datetime
from django.views import generic

from weather.models import City
from .forms import City_form


def index(request):
    return render(request, 'index.html')

def weather(request):
    url_info = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ed3d7827db074af8688ea192b0c67f52'
    url_detail = 'https://openweathermap.org/city/{}'

    if request.method == 'POST':
        form = City_form(request.POST)
        form.save()

    form = City_form()

    cities = City.objects.all()

    current_time = datetime.today().strftime("%H:%M")
    current_data = datetime.today().strftime("%d | %B | %Y")

    all_cities = []
    all_error = []
    for city in cities:
        res_info = requests.get(url_info.format(city.name)).json()
        if res_info["cod"] == "404":
            text_error = {
                'error': "The city name is entered incorrectly! Try again."
            }
            all_error.append(text_error)
            continue
        else:
            res_detail = url_detail.format(res_info["id"])
            city_info = {
                'city': res_info["name"],
                'temp': int(res_info["main"]["temp"]),
                'icon': res_info["weather"][0]["icon"],
                'time': current_time,
                'data': current_data,
                'id': res_detail
            }
            all_cities.append(city_info)
            all_error.clear()

    widget_cities = reversed(all_cities[-3:])
    context = {'all_info': widget_cities, 'form': form}
    if len(all_error) >= 1:
        error = all_error[0]['error']
        context['error'] = error

    return render(request, 'weather/weather.html', context)

def weather_clear(request):
    if request.method == 'GET':
        City.objects.all().delete()

    return weather(request)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
