from django.shortcuts import render
from django.views.decorators.cache import cache_control
from .models import ExplicitPurchase, Purchase, Item, Category

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    purchase = ExplicitPurchase.objects.all()
    print(purchase)
    context = {
        "purchase": purchase
    }
    print(context)
    return render(request, 'inventory/html/home.html', context)