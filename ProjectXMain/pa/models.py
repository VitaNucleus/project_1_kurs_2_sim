import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class TblAddresses(models.Model):
    adr_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, db_column="address_uuid", editable=False)
    adr_city = models.CharField(max_length=25, db_column="adr_city", verbose_name=_("Город"), blank=True, null=True)
    adr_street = models.CharField(max_length=50, db_column="adr_street", verbose_name=_("Улица"), blank=True,
                                  null=True)
    adr_district = models.CharField(max_length=50, db_column="adr_district", verbose_name=_("Район"), blank=True,
                                    null=True)
    adr_sub_district = models.CharField(max_length=50, db_column="adr_sub_district", verbose_name=_("Микрорайон"),
                                        blank=True, null=True)
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


class TblCianSale(models.Model):
    tcs_id = models.AutoField(primary_key=True, db_column="tcs_id")
    tcs_address = models.ForeignKey(TblAddresses, on_delete=models.DO_NOTHING, db_column="tcs_address", blank=True,
                                   null=True)
    tcs_url = models.URLField(db_column="tcs_url", verbose_name=_("URL"), blank=True, null=True)
    tcs_area = models.FloatField(max_length=25, db_column="tcs_area", verbose_name=_("Площадь"), blank=True, null=True)
    tcs_floor = models.FloatField(max_length=25, db_column="tcs_floor", verbose_name=_("Этаж"), blank=True, null=True)
    tcs_floors = models.FloatField(max_length=25, db_column="tcs_floors", verbose_name=_("Этажность"), blank=True,
                                  null=True)
    tcs_additional_info = models.JSONField(db_column="tcs_additional_info", verbose_name=_("Дополнительная информация"),
                                          blank=True, null=True)
    tcs_cost = models.FloatField(max_length=25, db_column="tcs_cost", verbose_name=_("Стоимость"), blank=True, null=True)

    class Meta:
        db_table = "tbl_cian_sale"
        verbose_name = _('Запись циана продажа')
        verbose_name_plural = _('Записи циана продажа')
        ordering = ['tcs_id']

class TblCianRent(models.Model):
    tcr_id = models.AutoField(primary_key=True, db_column="tcr_id")
    tcr_address = models.ForeignKey(TblAddresses, on_delete=models.DO_NOTHING, db_column="tcr_address", blank=True,
                                   null=True)
    tcr_url = models.URLField(db_column="tcr_url", verbose_name=_("URL"), blank=True, null=True)
    tcr_area = models.FloatField(max_length=25, db_column="tcr_area", verbose_name=_("Площадь"), blank=True, null=True)
    tcr_floor = models.FloatField(max_length=25, db_column="tcr_floor", verbose_name=_("Этаж"), blank=True, null=True)
    tcr_floors = models.FloatField(max_length=25, db_column="tcr_floors", verbose_name=_("Этажность"), blank=True,
                                  null=True)
    tcr_additional_info = models.JSONField(db_column="tcr_additional_info", verbose_name=_("Дополнительная информация"),
                                          blank=True, null=True)
    tcr_cost = models.FloatField(max_length=25, db_column="tcr_cost", verbose_name=_("Стоимость"), blank=True, null=True)

    class Meta:
        db_table = "tbl_cian_rent"
        verbose_name = _('Запись циан аренда')
        verbose_name_plural = _('Записи циана аренда')
        ordering = ['tcr_id']