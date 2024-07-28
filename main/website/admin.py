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


class BankAccountAdmin(admin.ModelAdmin):
    list_display = (
        "account_number",
        "customer",
        "bank_name",
        "bank_address",
        "account_type",
        "balance",
        "created_at",
        "updated_at",
    )


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(Banker)
