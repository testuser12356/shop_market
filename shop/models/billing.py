from django.db import models


class BillingInfo(models.Model):
    order = models.ForeignKey("Order", on_delete=models.SET_NULL, null=True, related_name="info")
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.EmailField(max_length=20)
    country = models.EmailField(max_length=50)
    street_address = models.EmailField(max_length=150)
    apartment_address = models.EmailField(max_length=150)
    town = models.EmailField(max_length=150)
    post_code = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name

    class Meta:
        db_table = "billing_info"
        ordering = ["-id"]


class ShippingAddress(BillingInfo):
    other_notes = models.TextField()

    def __str__(self):
        return self.f_name

    class Meta:
        db_table = "shipping_address"
        ordering = ["-id"]
