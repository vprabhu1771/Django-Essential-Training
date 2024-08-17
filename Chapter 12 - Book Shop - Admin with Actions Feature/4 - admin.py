from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'id', 'article_count',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # You can customize the queryset here, e.g., add annotations or filters
        return qs.filter(is_published=False)

    def mark_as_featured(self, request, queryset):
        queryset.update(is_published=True)

    mark_as_featured.short_description = 'Mark selected category as published'

    actions = [mark_as_featured]

admin.site.register(Category,CategoryAdmin)