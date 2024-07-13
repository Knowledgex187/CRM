from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import Customer, BankAccount, COUNTRY_CHOICES, Banker

# Imports messages to catch errors responses
from django.contrib import messages


from django.core.validators import validate_email

from django.contrib.auth import authenticate, login, logout as auth_logout

from django.contrib.auth.decorators import login_required

from django.db.models import Q


# Create your views here.

SpecialSym = set("!£$%^&*()?@;:~`¬-=_+")

"""Renders Home Page"""


@login_required(login_url="login")
def home(request):
    return render(request, "profile.html")


"""Login Form"""


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        user_login = authenticate(username=username, password=password)

        if user_login is not None:
            login(request, user_login)
            return redirect("profile")
        else:
            messages.info(request, "Credentials Invalid!")
            return redirect("login")
    else:
        return render(request, "login.html")


"""Signup Form"""


def signup(request):

    if request.method == "POST":
        username = request.POST.get("email", "").strip()
        first_name = request.POST.get("firstName", "").strip()
        last_name = request.POST.get("lastName", "").strip()
        password = request.POST.get("password", "").strip()
        password1 = request.POST.get("password1", "").strip()

        if not all([username, first_name, last_name, password, password1]):
            messages.info(request, "All fields required")
            return redirect("signup")

        if password != password1:
            messages.info(request, "Passwords do not match!")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.info(request, "User already exists!")
            return redirect("signup")

        if len(username) < 7:
            messages.info(request, "Email must be longer than 6 characters!")
            return redirect("signup")

        if len(first_name) < 3:
            messages.info(
                request, "First Name must contain more than 2 characters!"
            )
            return redirect("signup")

        if len(last_name) < 3:
            messages.info(
                request, "Last Name must contain more than 2 characters!"
            )
            return redirect("signup")

        # First name letters only parameters
        if not first_name.isalpha():
            messages.info(request, "First Name must be letters only!")
            return redirect("signup")

        # Last name letters only parameters
        if not last_name.isalpha():
            messages.info(request, "Last Name must be letters only!")
            return redirect("signup")

        # Password Numerical value parameters
        if not any(char.isdigit() for char in password):
            messages.info(request, "Password must contain a numerical value!")
            return redirect("signup")

        # Password capital letter parameters
        if not any(char.isupper() for char in password):
            messages.info(request, "Password must contain a capital letter!")
            return redirect("signup")

        # Password Special Character parameters
        if not any(char in SpecialSym for char in password):
            messages.info(request, "Password must contain a special Character")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.save()

        user_login = authenticate(username=username, password=password)
        if user_login:
            login(request, user_login)
            return redirect("profile")
        else:
            messages.info(request, "Authentication failed!")
            return redirect("signup")

    return render(request, "signup.html")


"""Add Customer"""


@login_required(login_url="login")
def add(request):
    content = {
        "country_choices": COUNTRY_CHOICES,
    }

    # All fields within the form!
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        first_name = request.POST.get("firstName", "").strip()
        middle_name = request.POST.get("middleName", "").strip()
        last_name = request.POST.get("lastName", "").strip()
        dob = request.POST.get("dob", "").strip()
        phone_number = request.POST.get("phoneNumber", "").strip()
        street_address = request.POST.get("streetAddress", "").strip()
        city = request.POST.get("city", "").strip()
        post_code_or_zip = request.POST.get("post_code_or_zip", "").strip()
        country = request.POST.get("country", "").strip()
        verified = request.POST.get("verifiedCheckbox") == "on"

        # Fields required backend
        if not all(
            [
                email,
                first_name,
                last_name,
                dob,
                phone_number,
                street_address,
                city,
                post_code_or_zip,
                country,
            ]
        ):
            messages.info(
                request, "All fields except Middle Name are required!"
            )
            return redirect("add")

        # Checks if Customer already exists
        if Customer.objects.filter(email=email).exists():
            messages.info(request, "Customer already exists!")
            return redirect("add")

        # Email length
        if len(email) < 7:
            messages.info(request, "Email must be longer than 6 characters!")
            return redirect("add")

        # Email validation
        try:
            validate_email(email)
        except ValidationError:
            messages.info(request, "Invalid email format!")
            return redirect("add")

        # First name parameters
        if len(first_name) < 3 or not first_name.isalpha():
            messages.info(
                request,
                "First Name must be more than two characters, and contain all letters!",
            )
            return redirect("add")

        # Last name parameters
        if len(last_name) < 3 or not last_name.isalpha():
            messages.info(
                request,
                "Last Name must be more than 2 characters, and contain all letters!",
            )
            return redirect("add")

        # Phone number parameters
        if not phone_number.isdigit() or len(phone_number) < 7:
            messages.info(
                request,
                "Phone number must be numerical values only, and be more than 6 digits!",
            )
            return redirect("add")

        # Street address length
        if len(street_address) < 3:
            messages.info(
                request, "Street address must be at least 3 characters !"
            )
            return redirect("add")

        # City length
        if len(city) < 2:
            messages.info(request, "City must be at least 2 characters!")
            return redirect("add")

        # Post Code length
        if len(post_code_or_zip) < 4:
            messages.info(
                request, "Zip/Post code must be more than 4 characters!"
            )
            return redirect("add")

        # Add new customer
        customer = Customer.objects.create(
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            dob=dob,
            phone_number=phone_number,
            street_address=street_address,
            city=city,
            post_code_or_zip=post_code_or_zip,
            country=country,
            verified=verified,
        )
        customer.save()
        messages.info(request, "Customer Added!")
        return redirect("bankaccount")

    return render(request, "add-customer.html", content)


"""Delete Customer"""


@login_required(login_url="login")
def delete_customer(request, pk):

    customer_uuid = pk
    customer = Customer.objects.get(uuid=customer_uuid)

    customer.delete()
    messages.info(
        request,
        f"{customer.first_name} {customer.last_name} has successfully been deleted!",
    )
    return redirect("view")


"""Delete Confirmation"""


@login_required(login_url="login")
def delete_confirm(request, pk):
    customer_uuid = pk
    customer = Customer.objects.get(uuid=customer_uuid)
    content = {
        "customer": customer,
    }

    if request.method == "POST":
        customer.delete()
        messages.info(
            request,
            f"{customer.first_name} {customer.last_name} has successfully been deleted!",
        )
        return redirect("view")

    return render(request, "delete-confirm.html", content)


def delete_account(request, pk):
    account_uuid = pk

    account = BankAccount.objects.get(uuid=account_uuid)

    content = {
        "account": account,
    }
    return render(request, "delete-confirm-account.html", content)


"""View & Edit Customer"""


@login_required(login_url="login")
def view_customer(request, pk):
    customer_uuid = pk
    customer_details = Customer.objects.get(uuid=customer_uuid)

    content = {
        "customer_details": customer_details,
        "country_choices": COUNTRY_CHOICES,
    }

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        first_name = request.POST.get("firstName", "").strip()
        middle_name = request.POST.get("middleName", "").strip()
        last_name = request.POST.get("lastName", "").strip()
        dob = request.POST.get("dob", "").strip()
        phone_number = request.POST.get("phoneNumber", "").strip()
        street_address = request.POST.get("streetAddress", "").strip()
        city = request.POST.get("city", "").strip()
        post_code_or_zip = request.POST.get("post_code_or_zip", "").strip()
        country = request.POST.get("country", "").strip()
        verified = request.POST.get("verifiedCheckbox") == "on"

        if len(email) < 7:
            messages.info(request, "Email must be longer than 6 characters!")
            return redirect("edit-customer", pk=pk)

        # Email validation
        try:
            validate_email(email)
        except ValidationError:
            messages.info(request, "Invalid email format!")
            return redirect("edit-customer", pk=pk)

        # First name parameters
        if len(first_name) < 3 or not first_name.isalpha():
            messages.info(
                request,
                "First Name must be more than two characters, and contain all letters!",
            )
            return redirect("edit-customer", pk=pk)

        # Last name parameters
        if len(last_name) < 3 or not last_name.isalpha():
            messages.info(
                request,
                "Last Name must be more than 2 characters, and contain all letters!",
            )
            return redirect("edit-customer", pk=pk)

        # Phone number parameters
        if not phone_number.isdigit() or len(phone_number) < 7:
            messages.info(
                request,
                "Phone number must be numerical values only, and be more than 6 digits!",
            )
            return redirect("edit-customer", pk=pk)

        # Street address length
        if len(street_address) < 3:
            messages.info(
                request, "Street address must be at least 3 characters !"
            )
            return redirect("edit-customer", pk=pk)

        # City length
        if len(city) < 2:
            messages.info(request, "City must be at least 2 characters!")
            return redirect("edit-customer", pk=pk)

        # Post Code length
        if len(post_code_or_zip) < 4:
            messages.info(
                request, "Zip/Post code must be more than 4 characters!"
            )
            return redirect("edit-customer", pk=pk)

        customer_details.email = email
        customer_details.first_name = first_name
        customer_details.middle_name = middle_name
        customer_details.last_name = last_name
        customer_details.dob = dob
        customer_details.phone_number = phone_number
        customer_details.street_address = street_address
        customer_details.city = city
        customer_details.post_code_or_zip = post_code_or_zip
        customer_details.country = country
        customer_details.verified = verified
        customer_details.save()

        messages.info(
            request,
            f"{customer_details.first_name} {customer_details.middle_name} {customer_details.last_name} details updated successfully!",
        )
        return redirect("edit-customer", pk=pk)

    return render(request, "customer-view.html", content)


"""View all customers"""


@login_required(login_url="login")
def customer_all(request):
    customers = Customer.objects.all()

    content = {
        "customers": customers,
    }

    return render(request, "customer-all.html", content)


"""Bank Account Post form"""


@login_required(login_url="login")
def bank_account(request):
    customers = Customer.objects.all()
    account_type = BankAccount.ACCOUNT_TYPES
    bank_name = BankAccount.BANK_NAME
    bank_address = BankAccount.BANK_ADDRESS

    content = {
        "customers": customers,
        "account_type": account_type,
        "bank_name": bank_name,
        "bank_address": bank_address,
    }

    if request.method == "POST":
        customer_uuid = request.POST.get("customer")
        account_type = request.POST.get("account")
        bank_name = request.POST.get("bankName")
        bank_address = request.POST.get("bankAddress")
        account_number = request.POST.get("accountNumber").strip()
        balance = request.POST.get("balance").strip()

        if not all(
            [
                customer_uuid,
                account_type,
                account_number,
                bank_name,
                bank_address,
                balance,
            ]
        ):
            messages.info(request, "All fields required!")
            return redirect("bankaccount")

        if BankAccount.objects.filter(account_number=account_number).exists():
            messages.info(request, "Bank account number already exists!")
            return redirect("bankaccount")

        if len(account_number) < 11 or not account_number.isdigit():
            messages.info(
                request,
                "Account number must be 11 digits and have numerical values only!",
            )
            return redirect("bankaccount")

        if not balance.isdigit():
            messages.info(request, "Balance must be numerical values only!")
            return redirect("bankaccount")

        # Get Customer in Customer model by ID
        customer = Customer.objects.get(uuid=customer_uuid)

        bank_account = BankAccount.objects.create(
            customer=customer,
            bank_name=bank_name,
            bank_address=bank_address,
            account_number=account_number,
            account_type=account_type,
            balance=balance,
        )
        bank_account.save()
        messages.info(request, "Bank details updated!")
        return redirect("banker")

    return render(request, "bank-account.html", content)


"""Banker Post Form"""


@login_required(login_url="login")
def banker(request):

    # Requests current user from default User module
    customers = Customer.objects.all()
    users = User.objects.all()
    current_user = request.user

    content = {
        "customers": customers,
        "users": users,
        "current_user": current_user,
    }

    if request.method == "POST":
        customer_uuid = request.POST.get("customer")
        user = request.user

        if not all(
            [
                customer_uuid,
            ]
        ):
            messages.info(request, "All fields required!")
            return redirect("banker")

        customer = Customer.objects.get(uuid=customer_uuid)

        if Banker.objects.filter(
            customer=customer,
            first_name=user.first_name,
            last_name=user.last_name,
        ).exists():
            messages.info(
                request,
                f"{customer.first_name} {customer.last_name} is already assigned to {user.first_name} {user.last_name}!",
            )
            return redirect("profile")

        bank = Banker.objects.create(
            customer=customer,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        bank.save()
        messages.info(request, "Banker assigned!")
        return redirect("profile")

    return render(request, "banker.html", content)


"""Edit Banker Profile Form """


@login_required(login_url="login")
def edit_profile(request):
    users = User.objects.all()
    current_user = request.user

    content = {
        "users": users,
        "current_user": current_user,
    }

    if request.method == "POST":
        first_name = request.POST.get("firstName", "").strip()
        last_name = request.POST.get("lastName", "").strip()
        active = request.POST.get("isActive", "").strip()
        joined = request.POST.get("dateJoined", "").strip()
        staff = request.POST.get("staff", "").strip()

        if not all(
            [
                first_name,
                last_name,
                active,
                joined,
                staff,
            ]
        ):
            messages.info(request, "All fields required!")
            return redirect("edit")

        if not (first_name.isalpha() and last_name.isalpha()):
            messages.info(request, "Names must be characters only!")
            return redirect("edit")

        current_user.first_name = first_name
        current_user.last_name = last_name
        current_user.is_active = active
        current_user.date_joined = joined
        current_user.is_staff = staff
        current_user.save()

    return render(request, "edit-profile.html", content)


"""Delete Profile"""


@login_required(login_url="login")
def delete_profile(request):

    current_user = request.user
    current_user.delete()
    messages.info(
        request,
        f"{current_user.first_name} {current_user.last_name} has successfully been deleted!",
    )
    return redirect("signup")


@login_required(login_url="login")
def delete_confirm_profile(request):

    if request.method == "POST":
        current_user = request.user
        current_user.delete()
        messages.info(
            request,
            f"{current_user.first_name} {current_user.last_name} has successfully been deleted!",
        )
        return redirect("signup")

    return render(request, "delete-confirm-profile.html")


@login_required(login_url="login")
def search_customer(request):
    customers = Customer.objects.all()
    if request.method == "GET":
        uuid = request.GET.get("uuid", "").strip()
        first_name = request.GET.get("firstName", "").strip()
        middle_name = request.GET.get("middleName", "").strip()
        last_name = request.GET.get("lastName", "").strip()
        dob = request.GET.get("dob", "").strip()
        phone_number = request.GET.get("phone", "").strip()
        email = request.GET.get("email", "").strip()
        street_address = request.GET.get("address", "").strip()
        city = request.GET.get("city", "").strip()
        post_code_or_zip = request.GET.get("zip", "").strip()
        country = request.GET.get("country", "").strip()

        filters = Q()
        if uuid:
            filters &= Q(uuid__icontains=uuid)
        if first_name:
            filters &= Q(first_name__icontains=first_name)
        if middle_name:
            filters &= Q(middle_name__icontains=middle_name)
        if last_name:
            filters &= Q(last_name__icontains=last_name)
        if dob:
            filters &= Q(dob__icontains=dob)
        if phone_number:
            filters &= Q(phone_number__icontains=phone_number)
        if email:
            filters &= Q(email__icontains=email)
        if street_address:
            filters &= Q(street_address__icontains=street_address)
        if city:
            filters &= Q(city__icontains=city)
        if post_code_or_zip:
            filters &= Q(post_code_or_zip__icontains=post_code_or_zip)
        if country:
            filters &= Q(country__icontains=country)

            customers = Customer.objects.filter(filters)

        content = {"customers": customers}
        return render(request, "customer-all.html", content)


@login_required(login_url="login")
def search_accounts(request):
    accounts = BankAccount.objects.all()
    if request.method == "GET":
        customer = request.GET.get("customer", "").strip()
        account_number = request.GET.get("accountNumber", "").strip()
        account_type = request.GET.get("accountType", "").strip()
        balance = request.GET.get("balance", "").strip()
        created_at = request.GET.get("created", "").strip()
        updated_at = request.GET.get("update", "").strip()

        filters = Q()

        if customer:
            filters &= Q(customer__icontains=customer)

        if account_number:
            filters &= Q(account_number__icontains=account_number)

        if account_type:
            filters &= Q(account_type__icontains=account_type)

        if balance:
            filters &= Q(balance__icontains=balance)

        if created_at:
            filters &= Q(created_at__icontains=created_at)

        if updated_at:
            filters &= Q(updated_at__icontains=updated_at)

            accounts = BankAccount.objects.filter(filters)

        content = {
            "accounts": accounts,
        }

        return render(request, "accounts.html", content)


"""Logout"""


@login_required(login_url="login")
def logout(request):
    auth_logout(request)
    messages.info(request, "You have logged out!")
    return redirect("login")
