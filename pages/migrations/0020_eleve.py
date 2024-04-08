# Generated by Django 4.0.6 on 2024-04-06 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_delete_eleve'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('classe', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='users/%y/%m/%d')),
            ],
        ),
    ]