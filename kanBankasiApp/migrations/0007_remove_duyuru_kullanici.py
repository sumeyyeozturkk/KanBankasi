# Generated by Django 2.0.4 on 2018-05-08 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanBankasiApp', '0006_auto_20180508_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duyuru',
            name='kullanici',
        ),
    ]