# Generated by Django 5.0.4 on 2024-04-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0024_alter_eleve_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='image1',
            field=models.ImageField(default='/users/default.png', upload_to='users/%y/%m/%d'),
        ),
    ]