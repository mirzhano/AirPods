from django.urls import path
from . import views

app_name = 'order'

urlpatterns =[
   path('', views.main_page, name="main_page"),
   path("show_detail/<int:id>/", views.show_details, name='show_detail'),
   path('add/', views.Create.as_view(), name= 'add'),
   path('order/<int:id>/delete', views.Delete.as_view(), name='delete'),
   path('order/<int:id>/update', views.Update.as_view(), name='update'),
]
