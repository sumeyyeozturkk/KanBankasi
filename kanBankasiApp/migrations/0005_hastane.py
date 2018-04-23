# Generated by Django 2.0.4 on 2018-04-23 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanBankasiApp', '0004_ilce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hastane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hastane_adi', models.CharField(max_length=100)),
                ('ilce_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kanBankasiApp.Ilce')),
            ],
        ),
    ]