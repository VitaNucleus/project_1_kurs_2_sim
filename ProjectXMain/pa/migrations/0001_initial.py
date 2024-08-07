# Generated by Django 5.0.3 on 2024-05-09 06:21

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblAddresses',
            fields=[
                ('adr_uuid', models.UUIDField(db_column='address_uuid', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('adr_city', models.CharField(blank=True, db_column='adr_city', max_length=25, null=True, verbose_name='Город')),
                ('adr_street', models.CharField(blank=True, db_column='adr_street', max_length=50, null=True, verbose_name='Улица')),
                ('adr_district', models.CharField(blank=True, db_column='adr_district', max_length=50, null=True, verbose_name='Район')),
                ('adr_sub_district', models.CharField(blank=True, db_column='adr_sub_district', max_length=50, null=True, verbose_name='Микрорайон')),
                ('adr_house', models.CharField(blank=True, db_column='adr_house', max_length=50, null=True, verbose_name='Дом')),
                ('adr_region', models.CharField(blank=True, db_column='adr_region', max_length=50, null=True, verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
                'db_table': 'tbl_address',
                'ordering': ['adr_city', 'adr_street'],
            },
        ),
        migrations.CreateModel(
            name='TblCian',
            fields=[
                ('tc_id', models.AutoField(db_column='tc_cian_record_id', primary_key=True, serialize=False)),
                ('tc_url', models.URLField(blank=True, db_column='tc_url', null=True, verbose_name='URL')),
                ('tc_area', models.FloatField(blank=True, db_column='tc_area', max_length=25, null=True, verbose_name='Площадь')),
                ('tc_floor', models.FloatField(blank=True, db_column='tc_floor', max_length=25, null=True, verbose_name='Этаж')),
                ('tc_floors', models.FloatField(blank=True, db_column='tc_floors', max_length=25, null=True, verbose_name='Этажность')),
                ('tc_additional_info', models.JSONField(blank=True, db_column='tc_additional_info', null=True, verbose_name='Дополнительная информация')),
                ('tc_rent_sale', models.CharField(blank=True, db_column='tc_rent_sale', max_length=4, null=True, verbose_name='Аренда или продожа')),
                ('tc_cost', models.FloatField(blank=True, db_column='tc_cost', max_length=25, null=True, verbose_name='Стоимость')),
                ('tc_address', models.ForeignKey(blank=True, db_column='tc_address', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pa.tbladdresses')),
            ],
            options={
                'verbose_name': 'Запись Циан',
                'verbose_name_plural': 'Записи Циана',
                'db_table': 'tbl_cian',
                'ordering': ['tc_id'],
            },
        ),
    ]
