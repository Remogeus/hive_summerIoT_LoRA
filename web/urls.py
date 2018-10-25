from django.urls import path
from .views import index, show_data

urlpatterns = [
    path('', index, name='index'),
    path('show_data', show_data, name='show_data'),
]
