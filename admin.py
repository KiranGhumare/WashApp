from django.contrib import admin
from .models import laundryshop, garment, Contact, Orders, OrderUpdate
admin.site.register(laundryshop)
admin.site.register(garment)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)