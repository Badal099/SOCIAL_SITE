# Generated by Django 3.2.6 on 2021-11-22 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_desc_post_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='status',
        ),
    ]
