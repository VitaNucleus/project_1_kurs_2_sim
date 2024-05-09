from django.urls import path
from .record_to_db import values_for_cian
from .views import Lk, json_test, enter




urlpatterns = [
    path('values_for_cian/', values_for_cian, name=('values_for_cian')),
    path('enter/', enter, name=('enter')),
    path('Lk/', Lk, name=('Lk')),
    path('test_json/', json_test, name=('test_json')),
]