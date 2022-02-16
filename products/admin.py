from django.contrib import admin
from .models import Product, Category, Rating


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
        'in_stock'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'product_id',
        'review_text',
        'number_of_stars',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
