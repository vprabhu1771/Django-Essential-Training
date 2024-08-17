# Chapter 17 - Django Built In Field Validation - help_text
 
![Image](1.PNG)

![Image](2.PNG)

3. open `models.py`

```
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
```

4. open `admin.py`

```
from django.contrib import admin
from .models import Author

# Register your models here.
admin.site.register(Author)
```