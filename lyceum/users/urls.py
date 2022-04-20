from django.contrib.auth.views import (
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path

from .views import LoginView, profile, signup, user_detail, user_list

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logout.html'),
        name='logout',
    ),
    path(
        'password-change/',
        PasswordChangeView.as_view(template_name='users/password_change.html'),
        name='password_change',
    ),
    path(
        'password-change-done/',
        PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'
        ),
        name='password_change_done',
    ),
    path(
        'password-reset/',
        PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset',
    ),
    path(
        'password-reset-done/',
        PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
        ),
        name='password_reset_done',
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset.html'
        ),
        name='password_reset_confirm',
    ),
    path(
        'password-reset-complete/',
        PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'
        ),
        name='password_reset_complete',
    ),
    path("users/", user_list),
    path("users/<int:user_num>/", user_detail, name='user_detail'),
    path("signup/", signup),
    path("profile/", profile, name='profile'),
]
