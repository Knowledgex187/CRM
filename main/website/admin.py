from django.contrib import admin
from .models import Customer, Banker, BankAccount


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "uuid",
        "first_name",
        "middle_name",
        "last_name",
        "email",
        "street_address",
        "city",
        "post_code_or_zip",
        "country",
    )


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(BankAccount)
admin.site.register(Banker)
