from django.urls import path, include
from . import views

urlpatterns = [
    # path("auth/signup/", views.signup, name="signup"),
    path("auth/", include("django.contrib.auth.urls")),
]
