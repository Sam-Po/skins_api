from django.contrib import admin
from market import models

admin.site.register(models.Order)
admin.site.register(models.Product)
admin.site.register(models.Cart)
admin.site.register(models.Category)
admin.site.register(models.OrderProduct)
