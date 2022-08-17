from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """
    # list_display = ('username', 'avatar', 'gender', 'language', 'currency', 'superhost')
    # list_filter = ('language', 'currency', 'superhost',)

    fieldsets = UserAdmin.fieldsets + (
        ("Custom profile",
         {"fields": (
            "avatar", 
            "gender", 
            "bio",
            "birthdate",
            "language",
            "currency",
            "superhost",
         )},
        ),
    )