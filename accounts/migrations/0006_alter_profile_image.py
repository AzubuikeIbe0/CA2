# Generated by Django 3.2.8 on 2021-11-01 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='timothy.jpg', null=True, upload_to='images/'),
        ),
    ]
