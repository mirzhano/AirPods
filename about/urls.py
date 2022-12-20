from django.urls import path
from . import views
urlpatterns=[
    path('', views.about, name='about_us'),
    path('add/', views.Create.as_view(), name= 'add'),
    path('about/<int:id>/delete', views.Delete.as_view(), name='delete'),
    path('about/<int:id>/update', views.Update.as_view(), name='update'),
    ]