# Generated by Django 4.0.6 on 2022-09-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flavor',
            field=models.CharField(max_length=200),
        ),
    ]
