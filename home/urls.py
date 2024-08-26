from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # http://127.0.0.1:8000/
    # path('', views.index),
    path('', views.register, name="register"),
    path('loadjson/', views.loadjason),
]