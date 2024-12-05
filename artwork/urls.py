from django.urls import path
from . import views

urlpatterns = [
    path('artworks/', views.artwork_list, name='artwork_list'),
]
