
from django.contrib import admin
from django.urls import path, include

from django101 import cities
from django101.cities.views import index, list_phones, test_index, create_person

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_index),
    path('create/', create_person, name='create person'),
    path('cities/', include('django101.cities.urls')),
    path('', include('django101.people.urls')),
]
