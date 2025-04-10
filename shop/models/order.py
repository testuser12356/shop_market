from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    payment_types = (
        ("transfer", "Direct Bank Transfer"),
        ("check_payments", "Check Payments"),
        ("cash", "Cash on Delivery"),
        ("paypal", "PayPal")
    )
    client = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, related_name="orders"
    )
    cart = models.ForeignKey("Cart", on_delete=models.SET_NULL, null=True, related_name="orders")
    total_sum = models.DecimalField(max_digits=16, decimal_places=2)
    payment_type = models.CharField(max_length=100, choices=payment_types, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order on {self.added_at}"

    class Meta:
        db_table = "orders"
        ordering = ("-id",)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE,
        related_name="items")
    product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL,
        null=True, related_name="order_items")
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    sum = models.DecimalField(max_digits=16, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order} item"

    class Meta:
        db_table = "order_items"
        ordering = ("order",)
