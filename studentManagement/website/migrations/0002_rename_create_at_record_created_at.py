# Generated by Django 4.2.7 on 2023-11-21 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
