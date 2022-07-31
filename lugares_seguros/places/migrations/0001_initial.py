# Generated by Django 4.0.6 on 2022-07-31 06:52

from django.db import migrations, models
import places.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('description', models.CharField(max_length=256)),
                ('address_state', models.CharField(max_length=32)),
                ('address_city', models.CharField(max_length=32)),
                ('address_colonia', models.CharField(max_length=32)),
                ('address_street', models.CharField(max_length=32)),
                ('address_zipcode', models.CharField(max_length=32)),
                ('image', models.ImageField(default='default.jpg', upload_to=places.models.upload_load)),
            ],
            options={
                'db_table': 'places',
            },
        ),
    ]