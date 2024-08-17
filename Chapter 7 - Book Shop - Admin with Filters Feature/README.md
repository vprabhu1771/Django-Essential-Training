# Chapter 7 - Book Shop - Admin with Filters Feature
 
![Image](1.PNG)

2. open `admin.py`

```
from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name','id')

    # Add filters for name field
    list_filter = ('name',)

    # Add search for name field
    search_fields = ('name',)

admin.site.register(Category,CategoryAdmin)
```