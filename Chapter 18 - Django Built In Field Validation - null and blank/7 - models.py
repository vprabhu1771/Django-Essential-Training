from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    dob = models.DateField(
        verbose_name="Date of Birth"
    )

    # Allow the email field to be null in the database and not required in forms.
    email = models.EmailField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"