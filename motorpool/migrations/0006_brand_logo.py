# Generated by Django 4.0.4 on 2022-08-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorpool', '0005_alter_vehiclepassport_auto'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='motorpool/brands/'),
        ),
    ]
