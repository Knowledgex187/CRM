from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="profile"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("add/", views.add, name="add"),
    path("edit-profile/", views.edit_profile, name="edit"),
]
