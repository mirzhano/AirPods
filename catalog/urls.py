from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

                  path("", views.main_page, name="main_page"),
                  path('main', views.main, name='main'),
                  path('about_us', views.about_us, name='about_us'),
                  path('index', views.home, name='index'),
                  path("show_detail/<int:id>/", views.show_details, name='show_detail'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
