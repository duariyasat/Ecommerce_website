from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('about/', views.about_view, name="about_view"),
    path('contact/', views.contact_view, name="contact_view"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)