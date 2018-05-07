# Generated by Django 2.0.4 on 2018-05-07 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanBankasiApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hastane',
            name='oneri',
        ),
        migrations.AlterField(
            model_name='hastane',
            name='eposta',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hastane',
            name='il',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kanBankasiApp.Il'),
        ),
        migrations.AlterField(
            model_name='hastane',
            name='ilce',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kanBankasiApp.Ilce'),
        ),
        migrations.AlterField(
            model_name='hastane',
            name='sifre',
            field=models.CharField(max_length=50),
        ),
    ]
