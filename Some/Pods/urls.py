from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import home

urlpatterns = [
# path('', views.home, name='home'),
path("", views.main_page, name="main_page"),
# path('air3/', views.air3, name='air3'),
path('about_us',views.about_us, name='about_us'),
path('index', views.home, name='index'),
path('characteristic/', views.characteristic, name='characterictic'),
path("show_detail/<int:id>/", views.show_details, name='show_detail'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
