from django.contrib import admin
from mptt.admin import MPTTModelAdmin

import shop.models as models


# Register your models here.

@admin.action(description="Copy")
def duplicate(modeladmin, request, queryset):
    for i in queryset:
        i.pk = None
        i.save()


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(MPTTModelAdmin):
    list_display = ("id", "name")


class ProductImageAdmin(admin.TabularInline):
    model = models.ProductImage
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions = [duplicate]
    inlines = [ProductImageAdmin]
    search_fields = ("title", "id")
    list_display_links = ("id",)
    list_filter = ("added_at", "category")
    list_editable = ("category", "title", "price",)
    list_display = ("id", "title", "category", "price", "added_at")


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    actions = [duplicate]
    list_editable = ("image",)
    list_display = ("id", "name", "image")


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    actions = [duplicate]
