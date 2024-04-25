# Generated by Django 5.0.3 on 2024-04-13 17:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbladdresses',
            name='adr_region',
            field=models.CharField(blank=True, db_column='adr_region', max_length=50, null=True, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='tbladdresses',
            name='id',
            field=models.UUIDField(db_column='address_uuid', default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
