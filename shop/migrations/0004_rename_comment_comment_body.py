# Generated by Django 3.2.9 on 2021-12-01 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
    ]
