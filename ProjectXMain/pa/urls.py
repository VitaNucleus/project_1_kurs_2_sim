from django.urls import path
from .record_to_db import values_for_cian
from .views import Lk, json_test, enter, Reg


urlpatterns = [
    path('home/', Lk, name='home'),
    path('test_json/', json_test, name='test_json'),
    path('values_for_cian/', values_for_cian, name='values_for_cian'),
]