# Generated by Django 5.0 on 2024-01-05 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_tbl_cart_tbl_complaint_tbl_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_complaint',
            name='shop',
        ),
        migrations.RemoveField(
            model_name='tbl_rating',
            name='food',
        ),
        migrations.RemoveField(
            model_name='tbl_rating',
            name='user',
        ),
        migrations.DeleteModel(
            name='tbl_cart',
        ),
        migrations.DeleteModel(
            name='tbl_complaint',
        ),
        migrations.DeleteModel(
            name='tbl_rating',
        ),
    ]