from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro, name="intro"),
    path("<int:num>/", views.calc, name="Calculate"),
    path("taxrate/", views.show_tax, name="show_tax")
]