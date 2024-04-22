from django.urls import path

from .views import RegisterView, PasswordChangeView, PasswordResetView, EmailConfirmationView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='sign_up'),
    path('change/', PasswordChangeView.as_view(), name='change_password'),
    path('reset/', PasswordResetView.as_view(), name='reset_password'),
    path('email/confirm/', EmailConfirmationView.as_view(), name='email_confirm'),
]