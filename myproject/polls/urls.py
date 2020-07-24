from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:cryptid_id>/", views.bio, name="detail"),
    path("locations/", views.locations, name="locations"),
    path("locations/<int:location_id>/", views.location, name="location"),
]