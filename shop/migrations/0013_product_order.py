# Generated by Django 3.2.8 on 2021-12-13 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_billing_status'),
        ('shop', '0012_product_users_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order_history', to='order.order'),
        ),
    ]
