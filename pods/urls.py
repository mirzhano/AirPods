from django.urls import path
from . import views
urlpatterns=[
    path('', views.header, name='header'),
    path("show_detail/<int:id>/", views.show_details, name='show_detail'),
]