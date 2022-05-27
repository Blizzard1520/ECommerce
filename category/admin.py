from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('tcg','ocg',)}  # Gợi ý trường slug theo category_name
    list_display = ('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
