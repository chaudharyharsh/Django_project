# Generated by Django 4.1.1 on 2022-10-06 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_orders"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Orders",
            new_name="Order",
        ),
    ]
