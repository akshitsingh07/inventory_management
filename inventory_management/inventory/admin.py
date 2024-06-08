from django.contrib import admin
from .models import Item, Purchase, Category, ExplicitPurchase

# Register your models here.
admin.site.register(Item)

admin.site.register(Purchase)

admin.site.register(Category)

admin.site.register(ExplicitPurchase)

admin.site.site_header = "ITC Inventory Administrative Panel"

admin.site.site_title = "ITC Inventory Administrative Panel"

admin.site.index_title = "Welcome Chief!"