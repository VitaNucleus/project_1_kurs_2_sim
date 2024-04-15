import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class TblAddresses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_column="address_uuid", editable=False)
    adr_city = models.CharField(max_length=25, db_column="adr_city", verbose_name=_("Город"), blank=True, null=True)
    adr_street = models.CharField(max_length=50, db_column="adr_street", verbose_name=_("Улица"), blank=True,
                                  null=True)
    adr_district = models.CharField(max_length=50, db_column="adr_district", verbose_name=_("Район"), blank=True,
                                    null=True)
    adr_house = models.CharField(max_length=50, db_column="adr_house", verbose_name=_("Дом"), blank=True, null=True)
    adr_region = models.CharField(max_length=50, db_column="adr_region", verbose_name=_("Регион"), blank=True,
                                  null=True)

    def __str__(self):
        address_string = _('г.%(city)s, ул.%(street)s, д.%(house)s') % {
            'city': self.adr_city,
            'street': self.adr_street,
            'house': self.adr_house
        }
        return address_string

    class Meta:
        db_table = 'tbl_address'
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')
        ordering = ['adr_city', 'adr_street']

class TblCian(models.Model):
    tc_id = models.AutoField(primary_key=True, db_column="tc_cian_record_id")
    tc_address = models.ForeignKey(TblAddresses, on_delete=models.DO_NOTHING, db_column="tc_address", blank=True,
                                   null=True)
    tc_url = models.URLField(db_column="tc_url", verbose_name=_("URL"), blank=True, null=True)
    tc_area = models.FloatField(max_length=25, db_column="tc_area", verbose_name=_("Площадь"), blank=True, null=True)
    tc_floor = models.FloatField(max_length=25, db_column="tc_floor", verbose_name=_("Этаж"), blank=True, null=True)
    tc_floors = models.FloatField(max_length=25, db_column="tc_floors", verbose_name=_("Этажность"), blank=True,
                                  null=True)
    tc_year_building = models.IntegerField(db_column="tc_year_building", verbose_name=_("Год постройки"),
                                           blank=True,null=True)
    tc_additional_info = models.JSONField(db_column="tc_additional_info", verbose_name=_("Дополнительная информация"),
                                          blank=True, null=True)

    class Meta:
        db_table = "tbl_cian"
        verbose_name = _('Запись Циан')
        verbose_name_plural = _('Записи Циана')
        ordering = ['tc_id']