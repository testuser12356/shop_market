from django.db import models
from django.contrib.auth.models import User


class Favorite(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="favorites")
    product = models.ForeignKey("Product",
                                on_delete=models.CASCADE,
                                related_name="user_favorites")

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "favorites"
        ordering = ("user",)
