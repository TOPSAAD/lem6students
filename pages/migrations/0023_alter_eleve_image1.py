# Generated by Django 5.0.4 on 2024-04-09 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0022_eleve_anniv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='image1',
            field=models.ImageField(default='/Users/mac/Desktop/lem6students/lem6students/static/images/default.png', upload_to='users/%y/%m/%d'),
        ),
    ]
