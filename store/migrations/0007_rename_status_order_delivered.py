# Generated by Django 4.1.1 on 2022-10-07 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_order_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="status",
            new_name="delivered",
        ),
    ]
