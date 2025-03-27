from django.contrib import admin

import users.models as models


# Register your models here.

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    ...
