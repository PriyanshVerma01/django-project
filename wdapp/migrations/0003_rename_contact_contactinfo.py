# Generated by Django 3.2.4 on 2021-08-25 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wdapp', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactInfo',
        ),
    ]
