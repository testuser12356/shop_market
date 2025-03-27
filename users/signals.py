from django.dispatch import receiver
from django.db.models.signals import post_save

import users.models as models


@receiver(post_save, sender=models.User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        models.UserProfile.objects.create(
            user=instance
        )
