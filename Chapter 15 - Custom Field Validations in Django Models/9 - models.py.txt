from django.db import models

from backend.validators import validate_author_gmail_mail

class Author(models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    dob = models.DateField(
        verbose_name="Date of Birth"
    )

    email = models.EmailField(
        validators=[validate_author_gmail_mail]
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"
