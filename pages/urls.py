from django.urls import path
from .views import HomePageView, contact_me


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', contact_me, name='contact'),
]

