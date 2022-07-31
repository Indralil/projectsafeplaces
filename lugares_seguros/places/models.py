from django.db import models

# Create your models here.

def upload_load(instance, filename):
    return f'photos_places/{instance.name}/{filename}'


class Place(models.Model):

    name = models.CharField(max_length=56)
    description = models.CharField(max_length=256)
    address_state = models.CharField(max_length=32)
    address_city = models.CharField(max_length=32)
    address_colonia = models.CharField(max_length=32)
    address_street = models.CharField(max_length=32)
    address_zipcode = models.CharField(max_length=32)
    image = models.ImageField(upload_to=upload_load, default='default.jpg', null=False)

    class Meta:
        db_table = 'places'

    def __str__(self):
        return self.name
