# Generated by Django 5.0.7 on 2024-09-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_delete_turfimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='turfdetails',
            name='image',
            field=models.ImageField(default='turf_images/default.jpg', upload_to='turf_images/'),
        ),
    ]
