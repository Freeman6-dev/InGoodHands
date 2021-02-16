from django.contrib import admin

# Register your models here.

from django.contrib import admin
from user_app.models import MyUser
from charity_donation_app.models import Institution


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass
