from django.urls import path
from . import views

app_name = 'bored_app'
urlpatterns = [
    path('', views.homePage, name="home"),
]
