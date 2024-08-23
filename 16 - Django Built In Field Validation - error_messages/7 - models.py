from django.db import models

# Create your models here.

class Country(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(
        max_length=255,
        unique=True,
        error_messages = {
            'unique': "Country Name is Already Exists"
        }
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'