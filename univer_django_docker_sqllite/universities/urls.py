from django.urls import path

from . import views

from django.urls import path
from .views import AddView, StatView

app_name = 'universities'
urlpatterns = [
    path('add/', AddView.as_view(), name='add'),
    path('stat/', StatView.as_view(), name='stat'),
]
