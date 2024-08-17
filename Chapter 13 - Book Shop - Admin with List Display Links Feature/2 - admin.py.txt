from django.contrib import admin
from .models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'id', 'article_count',)

    # Specify 'name' as the field to be linked to the change view
    list_display_links = ('id', 'description')

admin.site.register(Category, CategoryAdmin)