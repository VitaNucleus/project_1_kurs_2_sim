from django.urls import path
from .record_to_db import values_for_cian
from .views import *


urlpatterns = [
    path('home/', Lk, name='home'),
    path('test_json/', json_test, name='test_json'),
    path('values_for_cian/', values_for_cian, name='values_for_cian'),
    path('home/recomendation_form/', recomendation_form, name="recomendation_form"),
    path('home/object_form/', get_user_object, name="object_form"),
    path('delete_unnecessary/', delete_unnecessary, name="delete_unnecessary"),
    path('split_sale_and_rent/', split_sale_and_rent, name="split_sale_and_rent"),
]