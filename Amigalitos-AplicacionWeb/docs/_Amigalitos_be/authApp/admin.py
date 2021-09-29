from django.contrib import admin
from .models.user import User
from .models.account import Account

# Register your models here.

admin.site.register(User)
admin.site.register(Account)