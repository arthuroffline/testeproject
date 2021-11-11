from django.contrib import admin
from django.urls import path , include 

from apps.home import urls as home_urls

urlpatterns = [
    path ( 'home/', include (home_urls)),

    path ('admin/', admin.site.urls),
]
