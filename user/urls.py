from django.urls import path

from .views import RegisterView, change_password, LogoutView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="sign_up"),
    path("change_password/", change_password, name="change_password"),
    path("logout/", LogoutView.as_view()),
]
