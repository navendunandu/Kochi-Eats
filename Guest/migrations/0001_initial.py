# Generated by Django 5.0 on 2023-12-30 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0005_tbl_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=10)),
                ('user_contact', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_gender', models.CharField(max_length=20)),
                ('user_address', models.TextField()),
                ('user_photo', models.FileField(upload_to='UserDocs/')),
                ('user_password', models.CharField(max_length=20)),
                ('user_status', models.IntegerField(default=0)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
