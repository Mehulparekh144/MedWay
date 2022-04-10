from unicodedata import name
from django.urls import path ,re_path
from . import views
import regex

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login , name='login'),
    path('register/',views.register , name='register'),
    path('details/' , views.details , name='details'),
    path('account/', views.account , name='account'),
    path('view/<given_id>',views.view , name='view'),
    path('pin/',views.pin, name='pin'),
    path('fetch/',views.pin, name='fetch'),
    path('add/',views.add,name='add'),
    path('adddetails/' , views.adddetails , name='details'),
]
