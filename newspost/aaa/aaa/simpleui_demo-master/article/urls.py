from django.urls import path
from . import views
urlpatterns = [
     path('', views.hangye, name='行业'),

 ]