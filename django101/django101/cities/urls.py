from django.urls import path

from django101.cities.views import index, list_phones, show_forms_demo
from django.views.generic import TemplateView
urlpatterns = [
    path('', index),
    path('phones/', list_phones),
    path('phones2/', TemplateView.as_view(template_name='phones.html')),
    path('forms/', show_forms_demo),
]
