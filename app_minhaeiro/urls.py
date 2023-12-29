from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.app_minhaeiro, name='app_minhaeiro'),
    path('new_card', views.new_card, name='new_card')   
]
