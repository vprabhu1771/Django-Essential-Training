from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'id', 'article_count',)

    def article_count(self, obj):
        return obj.article_set.count()

    # Custom column name
    article_count.short_description = 'Number of Articles'

admin.site.register(Category,CategoryAdmin)