from django.db import models
import uuid


# Create your models here.

# List of countries as choices
COUNTRY_CHOICES = [
    ("Afghanistan", "Afghanistan"),
    ("Albania", "Albania"),
    ("Algeria", "Algeria"),
    ("Andorra", "Andorra"),
    ("Angola", "Angola"),
    ("Antigua and Barbuda", "Antigua and Barbuda"),
    ("Argentina", "Argentina"),
    ("Armenia", "Armenia"),
    ("Australia", "Australia"),
    ("Austria", "Austria"),
    ("Azerbaijan", "Azerbaijan"),
    ("Bahamas", "Bahamas"),
    ("Bahrain", "Bahrain"),
    ("Bangladesh", "Bangladesh"),
    ("Barbados", "Barbados"),
    ("Belarus", "Belarus"),
    ("Belgium", "Belgium"),
    ("Belize", "Belize"),
    ("Benin", "Benin"),
    ("Bhutan", "Bhutan"),
    ("Bolivia", "Bolivia"),
    ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
    ("Botswana", "Botswana"),
    ("Brazil", "Brazil"),
    ("Brunei", "Brunei"),
    ("Bulgaria", "Bulgaria"),
    ("Burkina Faso", "Burkina Faso"),
    ("Burundi", "Burundi"),
    ("Cabo Verde", "Cabo Verde"),
    ("Cambodia", "Cambodia"),
    ("Cameroon", "Cameroon"),
    ("Canada", "Canada"),
    ("Central African Republic", "Central African Republic"),
    ("Chad", "Chad"),
    ("Chile", "Chile"),
    ("China", "China"),
    ("Colombia", "Colombia"),
    ("Comoros", "Comoros"),
    ("Congo (Congo-Brazzaville)", "Congo (Congo-Brazzaville)"),
    ("Costa Rica", "Costa Rica"),
    ("Croatia", "Croatia"),
    ("Cuba", "Cuba"),
    ("Cyprus", "Cyprus"),
    ("Czech Republic (Czechia)", "Czech Republic (Czechia)"),
    (
        "Democratic Republic of the Congo",
        "Democratic Republic of the Congo",
    ),
    ("Denmark", "Denmark"),
    ("Djibouti", "Djibouti"),
    ("Dominica", "Dominica"),
    ("Dominican Republic", "Dominican Republic"),
    ("East Timor (Timor-Leste)", "East Timor (Timor-Leste)"),
    ("Ecuador", "Ecuador"),
    ("Egypt", "Egypt"),
    ("El Salvador", "El Salvador"),
    ("Equatorial Guinea", "Equatorial Guinea"),
    ("Eritrea", "Eritrea"),
    ("Estonia", "Estonia"),
    ("Eswatini (fmr. Swaziland)", "Eswatini (fmr. Swaziland)"),
    ("Ethiopia", "Ethiopia"),
    ("Fiji", "Fiji"),
    ("Finland", "Finland"),
    ("France", "France"),
    ("Gabon", "Gabon"),
    ("Gambia", "Gambia"),
    ("Georgia", "Georgia"),
    ("Germany", "Germany"),
    ("Ghana", "Ghana"),
    ("Greece", "Greece"),
    ("Grenada", "Grenada"),
    ("Guatemala", "Guatemala"),
    ("Guinea", "Guinea"),
    ("Guinea-Bissau", "Guinea-Bissau"),
    ("Guyana", "Guyana"),
    ("Haiti", "Haiti"),
    ("Honduras", "Honduras"),
    ("Hungary", "Hungary"),
    ("Iceland", "Iceland"),
    ("India", "India"),
    ("Indonesia", "Indonesia"),
    ("Iran", "Iran"),
    ("Iraq", "Iraq"),
    ("Ireland", "Ireland"),
    ("Israel", "Israel"),
    ("Italy", "Italy"),
    ("Jamaica", "Jamaica"),
    ("Japan", "Japan"),
    ("Jordan", "Jordan"),
    ("Kazakhstan", "Kazakhstan"),
    ("Kenya", "Kenya"),
    ("Kiribati", "Kiribati"),
    ("Korea, North", "Korea, North"),
    ("Korea, South", "Korea, South"),
    ("Kosovo", "Kosovo"),
    ("Kuwait", "Kuwait"),
    ("Kyrgyzstan", "Kyrgyzstan"),
    ("Laos", "Laos"),
    ("Latvia", "Latvia"),
    ("Lebanon", "Lebanon"),
    ("Lesotho", "Lesotho"),
    ("Liberia", "Liberia"),
    ("Libya", "Libya"),
    ("Liechtenstein", "Liechtenstein"),
    ("Lithuania", "Lithuania"),
    ("Luxembourg", "Luxembourg"),
    ("Madagascar", "Madagascar"),
    ("Malawi", "Malawi"),
    ("Malaysia", "Malaysia"),
    ("Maldives", "Maldives"),
    ("Mali", "Mali"),
    ("Malta", "Malta"),
    ("Marshall Islands", "Marshall Islands"),
    ("Mauritania", "Mauritania"),
    ("Mauritius", "Mauritius"),
    ("Mexico", "Mexico"),
    ("Micronesia", "Micronesia"),
    ("Moldova", "Moldova"),
    ("Monaco", "Monaco"),
    ("Mongolia", "Mongolia"),
    ("Montenegro", "Montenegro"),
    ("Morocco", "Morocco"),
    ("Mozambique", "Mozambique"),
    ("Myanmar (formerly Burma)", "Myanmar (formerly Burma)"),
    ("Namibia", "Namibia"),
    ("Nauru", "Nauru"),
    ("Nepal", "Nepal"),
    ("Netherlands", "Netherlands"),
    ("New Zealand", "New Zealand"),
    ("Nicaragua", "Nicaragua"),
    ("Niger", "Niger"),
    ("Nigeria", "Nigeria"),
    (
        "North Macedonia (formerly Macedonia)",
        "North Macedonia (formerly Macedonia)",
    ),
    ("Norway", "Norway"),
    ("Oman", "Oman"),
    ("Pakistan", "Pakistan"),
    ("Palau", "Palau"),
    ("Panama", "Panama"),
    ("Papua New Guinea", "Papua New Guinea"),
    ("Paraguay", "Paraguay"),
    ("Peru", "Peru"),
    ("Philippines", "Philippines"),
    ("Poland", "Poland"),
    ("Portugal", "Portugal"),
    ("Qatar", "Qatar"),
    ("Romania", "Romania"),
    ("Russia", "Russia"),
    ("Rwanda", "Rwanda"),
    ("Saint Kitts and Nevis", "Saint Kitts and Nevis"),
    ("Saint Lucia", "Saint Lucia"),
    (
        "Saint Vincent and the Grenadines",
        "Saint Vincent and the Grenadines",
    ),
    ("Samoa", "Samoa"),
    ("San Marino", "San Marino"),
    ("Sao Tome and Principe", "Sao Tome and Principe"),
    ("Saudi Arabia", "Saudi Arabia"),
    ("Senegal", "Senegal"),
    ("Serbia", "Serbia"),
    ("Seychelles", "Seychelles"),
    ("Sierra Leone", "Sierra Leone"),
    ("Singapore", "Singapore"),
    ("Slovakia", "Slovakia"),
    ("Slovenia", "Slovenia"),
    ("Solomon Islands", "Solomon Islands"),
    ("Somalia", "Somalia"),
    ("South Africa", "South Africa"),
    ("South Sudan", "South Sudan"),
    ("Spain", "Spain"),
    ("Sri Lanka", "Sri Lanka"),
    ("Sudan", "Sudan"),
    ("Suriname", "Suriname"),
    ("Sweden", "Sweden"),
    ("Switzerland", "Switzerland"),
    ("Syria", "Syria"),
    ("Taiwan", "Taiwan"),
    ("Tajikistan", "Tajikistan"),
    ("Tanzania", "Tanzania"),
    ("Thailand", "Thailand"),
    ("Togo", "Togo"),
    ("Tonga", "Tonga"),
    ("Trinidad and Tobago", "Trinidad and Tobago"),
    ("Tunisia", "Tunisia"),
    ("Turkey", "Turkey"),
    ("Turkmenistan", "Turkmenistan"),
    ("Tuvalu", "Tuvalu"),
    ("Uganda", "Uganda"),
    ("Ukraine", "Ukraine"),
    ("United Arab Emirates", "United Arab Emirates"),
    ("United Kingdom", "United Kingdom"),
    ("United States", "United States"),
    ("Uruguay", "Uruguay"),
    ("Uzbekistan", "Uzbekistan"),
    ("Vanuatu", "Vanuatu"),
    ("Vatican City (Holy See)", "Vatican City (Holy See)"),
    ("Venezuela", "Venezuela"),
    ("Vietnam", "Vietnam"),
    ("Yemen", "Yemen"),
    ("Zambia", "Zambia"),
    ("Zimbabwe", "Zimbabwe"),
]


class Customer(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    street_address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    post_code_or_zip = models.CharField(max_length=20)
    country = models.CharField(
        max_length=100, choices=COUNTRY_CHOICES, default="United Kingdom"
    )
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}".strip()


class BankAccount(models.Model):
    ACCOUNT_TYPES = [
        ("Savings", "Savings"),
        ("Checking", "Checking"),
        ("Business", "Business"),
    ]

    BANK_NAME = [
        ("IBF", "IBF"),
    ]

    BANK_ADDRESS = [
        (
            "P.O. BOX 802 Grand Cayman KY1-1100 CAYMAN ISLANDS",
            "P.O. BOX 802 Grand Cayman KY1-1100 CAYMAN ISLANDS",
        ),
    ]

    account_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="bank_accounts"
    )
    bank_name = models.CharField(
        max_length=255, choices=BANK_NAME, default="IBF"
    )
    bank_address = models.TextField(choices=BANK_ADDRESS)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    balance = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.bank_name} ({self.account_type})"


class Banker(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} (Customer: {self.customer})"
        )
