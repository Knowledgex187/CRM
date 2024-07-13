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
    path("view-customers/", views.customer_all, name="view"),
    path("customer/<uuid:pk>/", views.view_customer, name="edit-customer"),
    path(
        "delete-customer/<uuid:pk>/",
        views.delete_customer,
        name="delete-customer",
    ),
    path("delete-profile/", views.delete_profile, name="delete-profile"),
    path(
        "confirm-delete/<uuid:pk>/",
        views.delete_confirm,
        name="delete-confirm",
    ),
    path(
        "delete-profile/",
        views.delete_profile,
        name="delete-profile",
    ),
    path(
        "delete-confirm/",
        views.delete_confirm_profile,
        name="delete-profile-confirm",
    ),
    path("search/", views.search_customer, name="search"),
    path("accounts-list/", views.search_accounts, name="accounts"),
    path(
        "confirm-delete-account/<uuid:pk>/",
        views.delete_account,
        name="delete-account-confirm",
    ),
]
