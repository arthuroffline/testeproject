from django.urls import path
from.views import HomeView
from django.views.generic.base import TemplateView

urlpatterns = [
    path ('', HomeView.as_view( ), name = 'home') 
    
]

