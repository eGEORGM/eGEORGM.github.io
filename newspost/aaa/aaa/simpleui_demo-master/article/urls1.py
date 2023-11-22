from django.urls import path
from . import views
urlpatterns = [
     path('',views.quyu,name='区域')
 ]