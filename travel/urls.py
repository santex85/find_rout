import namespace as namespace
from django.contrib import admin
from django.urls import path, include

from travel.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # change for home page
    path('cities/', include(('cities.urls', 'cities'))),
]
