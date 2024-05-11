from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(TblAddresses)
class TblAddressesAdmin(admin.ModelAdmin):
    list_display = ['adr_city', 'adr_street', 'adr_house']
    search_fields = ['adr_city', 'adr_street', 'adr_house']
    list_per_page = 25


@admin.register(TblCianSale)
class TblCianAdmin(admin.ModelAdmin):
    list_display = ['tcs_url', 'tcs_area']
    search_fields = ['tcs_url', 'tcs_area']
    list_per_page = 25


@admin.register(TblCianRent)
class TblCianAdmin(admin.ModelAdmin):
    list_display = ['tcr_url', 'tcr_area']
    search_fields = ['tcr_url', 'tcr_area']
    list_per_page = 25