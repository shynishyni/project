# Generated by Django 5.0.7 on 2024-09-30 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_turfdetails_image1_alter_turfdetails_image2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turfdetails',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='turfdetails',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='turfdetails',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='turfdetails',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='turfdetails',
            name='image5',
        ),
        migrations.AddField(
            model_name='turfdetails',
            name='images',
            field=models.JSONField(default=list),
        ),
    ]
