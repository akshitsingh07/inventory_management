from django.shortcuts import render
from django.views.decorators.cache import cache_control
from .models import ExplicitPurchase, Purchase, Item, Category

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    purchase = ExplicitPurchase.objects.all()
    low_quantity_items = purchase.filter(quantity__lt=10)
    low_quantity_count = low_quantity_items.count()
    print(purchase)
    context = {
        "purchase": purchase,
        'low_quantity_items': low_quantity_items,
        "low_quantity_count": low_quantity_count
    }
    print(context)
    return render(request, 'inventory/html/home.html', context)