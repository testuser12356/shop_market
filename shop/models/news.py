from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to="news/%Y-%m-%d")
    title = models.CharField(max_length=255)
    post = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "news"
        ordering = ["-added_at"]
