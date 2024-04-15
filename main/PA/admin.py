from django.contrib import admin
from .models import TblCian, TblAddresses

# Register your models here.
@admin.register(TblAddresses)
class TblAddressesAdmin(admin.ModelAdmin):
    list_display = ['adr_city', 'adr_street', 'adr_house']
    search_fields = ['adr_city', 'adr_street', 'adr_house']
    list_per_page = 25

@admin.register(TblCian)
class TblCianAdmin(admin.ModelAdmin):
    list_display = ['tc_url', 'tc_area', 'tc_year_building']
    search_fields = ['tc_url', 'tc_area']
    list_per_page = 25