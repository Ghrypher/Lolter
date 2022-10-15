from django.urls import path 
from . import views

#Aca fijo todos los links o urls relacionados con myapp, de esta forma, no tengo todas las urls
#de mi pagina en una misma lista enorme ubicada en mysite/urls.py
urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
]