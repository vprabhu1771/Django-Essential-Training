from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    dob = models.DateField(
        help_text="Please use the following format: <em>YYYY-MM-DD</em>."
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"