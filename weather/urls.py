from django.contrib import admin
from django.urls import path, include
from weather.views import weather, SignUpView, index, weather_clear

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('weather/', weather, name='weather'),
    path('weather_clear/', weather_clear, name='weather_clear')
]