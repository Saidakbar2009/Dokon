# Generated by Django 4.2.5 on 2023-11-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='tasdiqlangan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profil',
            name='tasdiqlash_kodi',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
