# Generated by Django 3.2.8 on 2021-11-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211111_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='timothy.jpg', null=True, upload_to='images/'),
        ),
    ]
