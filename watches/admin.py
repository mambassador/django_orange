from django.contrib import admin

from .models import Brand, Designer, Store, Watch


@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name__startswith",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    list_filter = ("country",)
    search_fields = ("name__startswith",)


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "brand", "colour", "size")
    list_filter = ("brand",)
    search_fields = ("name__startswith",)
    fieldsets = (("Basic Information", {"fields": ("name", "price", "brand", "colour", "size")}),)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("watches",)
    search_fields = ("name__startswith",)
