from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="brand-images/%Y-%m-%d")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "brands"
        ordering = ["name"]
