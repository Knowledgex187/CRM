from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="profile"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("add/", views.add, name="add"),
    path("edit-profile/", views.edit_profile, name="edit"),
    path("bank-account/", views.bank_account, name="bankaccount"),
    path("assign-banker/", views.banker, name="banker"),
    path("view-customers/", views.view_customers, name="view"),
]
