# Generated by Django 5.0.2 on 2024-02-24 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_tbl_complaint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_cart',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='tbl_cart',
            name='food',
        ),
        migrations.DeleteModel(
            name='tbl_booking',
        ),
        migrations.DeleteModel(
            name='tbl_cart',
        ),
    ]