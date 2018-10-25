from django.urls import path
from .views import device, message

urlpatterns = [
    path('device', device, name='device'),
    path('message', message, name='message')
]
