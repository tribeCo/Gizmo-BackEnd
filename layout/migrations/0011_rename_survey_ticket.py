# Generated by Django 4.2.7 on 2024-03-10 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0010_survey'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Survey',
            new_name='Ticket',
        ),
    ]