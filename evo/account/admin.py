from django.contrib import admin
from .models import Products,Cart,Orders,Services,Scart,Status

# Register your models here.

admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Services)
admin.site.register(Scart)
admin.site.register(Status)