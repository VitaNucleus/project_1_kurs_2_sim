from django.urls import path
from .views import login_users, logout_users, registration


urlpatterns = [
    path('registration/', registration, name='Reg'),
    path('login/', login_users, name='login'),
    path('logout/', logout_users, name='logout'),
]
