# Generated by Django 3.2.9 on 2021-12-01 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_voucher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=80)),
                ('user_email', models.EmailField(default='', max_length=254)),
                ('user_url', models.URLField(default='')),
                ('comment', models.TextField(default='')),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('ip_public', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
                ('content_type_id', models.IntegerField()),
                ('site_id', models.BigIntegerField()),
                ('object_pk', models.TextField()),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.product')),
            ],
            options={
                'ordering': ['submit_date'],
            },
        ),
    ]
