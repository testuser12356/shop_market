# Generated by Django 4.2.20 on 2025-04-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_billinginfo_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('transfer', 'Direct Bank Transfer'), ('check_payments', 'Check Payments'), ('cash', 'Cash on Delivery'), ('paypal', 'PayPal')], max_length=100, null=True),
        ),
    ]
