from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    custom_item_id = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.custom_item_id})"

class Purchase(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_of_purchase = models.DateField()
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Purchase of {self.quantity} {self.item.name}(s) on {self.date_of_purchase} costing {self.cost}"

# To define the fields explicitly
class ExplicitPurchase(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    custom_item_id = models.CharField(max_length=50)  # Renamed to avoid conflict
    date_of_purchase = models.DateField()
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Purchase of {self.quantity} {self.item.name}(s) ({self.custom_item_id}) on {self.date_of_purchase} costing {self.cost}"
