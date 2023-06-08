from django.contrib import admin
<<<<<<< HEAD
from .models import Product, Category, Comment

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comment)
=======
from .models import Category, Product, Profile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_data', 'phone')
    list_filter = ('birth_data',)
    search_fields = ('user__username', 'user__email')
>>>>>>> d3bd320 (ShopTestDj)
