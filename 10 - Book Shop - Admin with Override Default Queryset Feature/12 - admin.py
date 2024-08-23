from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'id',)

    # Add filters for name field
    list_filter = ('name',)

    # Add search for name field
    search_fields = ('name',)

    # Sorting by name in ascending order
    # ordering = ['name']

    # To sort by name in descending order, use the negative sign
    ordering = ['-name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # You can customize the queryset here, e.g., add annotations or filters
        return qs.filter(is_published=False)

admin.site.register(Category,CategoryAdmin)