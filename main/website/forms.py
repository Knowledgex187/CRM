from django import forms
from .models import COUNTRY_CHOICES, Customer, BankAccount, Banker


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "DOB",
            "phone_number",
            "email",
            "street_address",
            "city",
            "post_code_or_zip",
            "country",
            "identity_verified",
            "picture",
        ]
        widgets = {
            "DOB": forms.SelectDateWidget(years=range(1900, 2023)),
            "country": forms.Select(choices=COUNTRY_CHOICES),
        }


class BankForm(forms.ModelForm):
    pass
