# Django-Essential-Training
 
1. open `models.py`

```
from django.db import models

class Category(models.Model):

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
```

2. open `admin.py`
```
from django.contrib import admin
from .models import Category

# Register your models here.
admin.site.register(Category)
```