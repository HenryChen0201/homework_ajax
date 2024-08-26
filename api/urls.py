from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # http://127.0.0.1:8000/api/register
    path('register/', views.register),
    # http://127.0.0.1:8000/api/check_name
    path('check_name/<str:name>/', views.check_name),
]