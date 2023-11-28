from django.contrib import admin

from .models import User, AddressUser

admin.site.register(User)
admin.site.register(AddressUser)