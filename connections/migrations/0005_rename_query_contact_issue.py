# Generated by Django 4.2.2 on 2023-07-07 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0004_rename_desc_contact_query'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='query',
            new_name='issue',
        ),
    ]