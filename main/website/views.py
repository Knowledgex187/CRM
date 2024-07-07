from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import User

from .models import Customer, BankAccount, Banker, COUNTRY_CHOICES

# Imports messages to catch errors responses
from django.contrib import messages

from .forms import CustomerForm

from django.core.validators import validate_email

from django.contrib.auth import authenticate, login, logout as auth_logout

# Create your views here.

SpecialSym = set("!£$%^&*()?@;:~`¬-=_+")


def home(request):
    return render(request, "profile.html")


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


def signup(request):

    if request.method == "POST":
        username = request.POST.get("email", "").strip()
        first_name = request.POST.get("firstName", "").strip()
        last_name = request.POST.get("lastName", "").strip()
        password = request.POST.get("password1", "").strip()
        password1 = request.POST.get("password2", "").strip()

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
            password=password,
            password1=password1,
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
        dob = request.POST.get("DOB", "").strip()
        phone_number = request.POST.get("phoneNumber", "").strip()
        street_address = request.POST.get("streetAddress", "").strip()
        city = request.POST.get("city", "").strip()
        zip_post = request.POST.get("post_code_or_zip", "").strip()
        country = request.POST.get("country", "").strip()

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
                zip_post,
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
            return redirect("signup")

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

        # Last name parameters
        if len(last_name) < 3 or not last_name.isalpha():
            messages.info(
                request,
                "Last Name must be more than 2 characters, and contain all letters!",
            )
            return redirect("add")

        # Middle name parameters
        if len(middle_name) < 3 or not middle_name.isalpha():
            messages.info(
                request,
                "Middle Name must be more than 2 characters, and contain all letters!",
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
        if len(zip_post) < 4:
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
            zip_post=zip_post,
            country=country,
        )
        customer.save()
        messages.info(request, "Customer Added!")
        return redirect("bankaccount")

    return render(request, "add-customer.html", content)


def view_customers(request):
    customers = Customer.objects.all()

    content = {
        "customers": customers,
    }

    pass


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
        customer = request.POST.get("customer")
        account_type = request.POST.get("account")
        bank_name = request.POST.get("bankName")
        bank_address = request.POST.get("bankAddress")
        account_number = request.POST.get("accountNumber").strip()
        balance = request.POST.get("balance").strip()

        if not all(
            [
                customer,
                account_type,
                account_number,
                bank_name,
                bank_address,
                balance,
            ]
        ):
            messages.info(request, "All fields required!")
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

        customer == Customer.objects.get(uuid=customer)

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


def banker(request):

    # Requests current user from default User module
    user = request.user

    content = {
        "user": user,
    }

    return render(request, "banker.html", content)


def edit_profile(request):
    customers = Customer.objects.all()
    selected_customer = None
    form = None

    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        if customer_id:
            selected_customer = get_object_or_404(Customer, id=customer_id)

            form = CustomerForm(
                request.POST, request.FILES, instance=selected_customer
            )

            if "delete-account" in request.POST:
                selected_customer.delete()
                messages.info(request, "Customer successfully deleted!")
                return redirect(
                    "edit"
                )  # Redirect to a success page after deletion

            if form.is_valid():
                form.save()
                messages.info(request, "Customer details updated!")
                return redirect(
                    "edit"
                )  # Redirect to a success page after saving

        else:
            CustomerForm(request.POST, request.FILES)

    if not form:
        form = CustomerForm()

    content = {
        "customers": customers,
        "form": form,
        "selected_customer": selected_customer,
    }

    return render(request, "edit-profile.html", content)


def logout(request):
    auth_logout(request)
    messages.info(request, "You have logged out!")
    return redirect("login")
