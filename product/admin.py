from django.contrib import admin
from .models import *

class AdminCustomer(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'contact_no', 'pincode']

admin.site.register(Customer, AdminCustomer)

class AdminProduct(admin.ModelAdmin):
	list_display = ['name', 'unit_price']

admin.site.register(Product, AdminProduct)

class AdminOrder(admin.ModelAdmin):
	list_diaplay = ['customer_id', 'product_id', 'qty', 'total_price', 'created_date']

admin.site.register(Order, AdminOrder)