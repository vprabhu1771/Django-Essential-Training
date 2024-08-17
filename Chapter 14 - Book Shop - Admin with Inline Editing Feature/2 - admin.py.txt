from django.contrib import admin
from .models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'article_count',)

    # Specify 'name' as the field to be linked to the change view
    list_display_links = ('id',)

    # Allow inline editing of the 'name' field
    list_editable = ('name',)

admin.site.register(Category, CategoryAdmin)