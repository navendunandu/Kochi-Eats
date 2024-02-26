# Generated by Django 5.0 on 2024-01-05 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_health'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tbl_cooperation',
            new_name='tbl_corporation',
        ),
        migrations.RenameField(
            model_name='tbl_corporation',
            old_name='cooperation_address',
            new_name='corporation_address',
        ),
        migrations.RenameField(
            model_name='tbl_corporation',
            old_name='cooperation_contact',
            new_name='corporation_contact',
        ),
        migrations.RenameField(
            model_name='tbl_corporation',
            old_name='cooperation_email',
            new_name='corporation_email',
        ),
        migrations.RenameField(
            model_name='tbl_corporation',
            old_name='cooperation_name',
            new_name='corporation_name',
        ),
        migrations.RenameField(
            model_name='tbl_corporation',
            old_name='cooperation_password',
            new_name='corporation_password',
        ),
    ]
