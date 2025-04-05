from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    is_active = models.BooleanField(default=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CART {self.added_at}"

    class Meta:
        db_table = "carts"
        ordering = ["user"]


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Cart Item: {self.cart}"

    class Meta:
        db_table = "cart_items"
        ordering = ["cart"]
