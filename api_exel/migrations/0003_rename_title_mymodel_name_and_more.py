# Generated by Django 4.1.7 on 2023-03-08 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_exel', '0002_rename_price_mymodel_my_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='mymodel',
            old_name='my_price',
            new_name='price',
        ),
    ]
