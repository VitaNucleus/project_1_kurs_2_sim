from django.urls import path
from .record_to_db import values_for_cian
from .views import test, json_test

urlpatterns = [
    path('values_for_cian/', values_for_cian, name=('values_for_cian')),
    path('test/', test, name=('test')),
    path('test_json/', json_test, name=('test_json')),
]