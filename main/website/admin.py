from django.contrib import admin
from .models import Customer, Banker, BankAccount

# Register your models here.
admin.site.register(Customer)
admin.site.register(BankAccount)
admin.site.register(Banker)
