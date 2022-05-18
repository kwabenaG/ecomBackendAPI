# handles the urls 

from django.urls import path, include 
from .views import SignUpUserView


urlpatterns = [
    path('auth/signup', SignUpUserView.as_view(), name='signup'),
]