from django_ecommerce_app.models import Categories
from django.contrib import admin
from django_ecommerce_app.models import Categories, SubCategories

# Register your models here.
admin.site.register(Categories)
admin.site.register(SubCategories)