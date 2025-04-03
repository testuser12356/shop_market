from django.db import models
from django_quill.fields import QuillField
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sizes"
        ordering = ["name"]


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "colors"
        ordering = ["name"]


class ProductCategory(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    order_num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['order_num']

    class Meta:
        db_table = "product_category"
        ordering = ["name"]


class Product(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    brand = models.ForeignKey("Brand",
                              on_delete=models.SET_NULL, null=True,
                              blank=True, related_name="products")
    category = TreeForeignKey(
        ProductCategory, on_delete=models.SET_NULL,
        null=True, related_name="categories")
    price = models.DecimalField(max_digits=16, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=16, decimal_places=2, null=True, blank=True)
    main_image = models.ImageField(upload_to="products/%Y-%m-%d")
    description = QuillField()
    details = QuillField()
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "products"
        ordering = ["-id"]


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product_images/%Y-%m-%d")

    def __str__(self):
        return f"{self.product.title} image"

    class Meta:
        db_table = "product_images"
        ordering = ["product"]
