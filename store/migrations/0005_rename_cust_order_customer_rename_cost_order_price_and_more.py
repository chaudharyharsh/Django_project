# Generated by Django 4.1.1 on 2022-10-06 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_rename_orders_order"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="cust",
            new_name="customer",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="cost",
            new_name="price",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="prod",
            new_name="product",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="quant",
            new_name="quantity",
        ),
    ]