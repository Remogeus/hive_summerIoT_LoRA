from django.urls import path
from .views import hive

urlpatterns = [
    path('device', device, name='device')
]
