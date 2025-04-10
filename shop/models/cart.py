from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    is_active = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)
    total_sum = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)

    def __str__(self):
        return f"CART {self.added_at}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        if self.items.all():
            total_sum = 0
            for i in self.items.all():
                total_sum += i.sum
            self.total_sum = total_sum
        super().save()

    class Meta:
        db_table = "carts"
        ordering = ["user"]


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    sum = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Cart Item: {self.cart}"

    class Meta:
        db_table = "cart_items"
        ordering = ["cart"]
