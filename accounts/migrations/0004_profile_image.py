# Generated by Django 3.2.8 on 2021-11-01 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211101_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.IntegerField(default=0, blank=True, editable=True),
        ),
    ]
