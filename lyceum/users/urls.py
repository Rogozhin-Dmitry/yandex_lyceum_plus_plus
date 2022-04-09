from django.urls import path

from .views import profile, signup, user_detail, user_list

urlpatterns = [
    path("users/", user_list),
    path("users/<int:user_num>/", user_detail),
    path("signup/", signup),
    path("profile/", profile),
]
