from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("login_page/", login_page, name='login_page'),
    path("signup_page/", signup_page, name='signup_page'),
    path("forgot_password_page/", forgot_password_page, name='forgot_password_page'),
    path("otp_page/", otp_page, name='otp_page'),
    path("profile_page/", profile_page),
    
    path("signup/", signup, name="signup"),
    path("forget_password/", forget_password, name="forget_password"),
    path("verify_otp/<str:verify_for>", verify_otp, name="verify_otp"),

    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("profile_update/", profile_update, name="profile_update"),
    path("profile_image_upload/", profile_image_upload, name="profile_image_upload"),
    path("add_expense/", add_expense, name="add_expense"),
    path("add_budget/", add_budget, name="add_budget"),
    path("delete_budget/<int:id>/", delete_budget, name="delete_budget"),
]