from django.urls import path
from .views import user_list, user_detail, signup, profile

urlpatterns = [
    path('users/', user_list),
    path('users/<int:user_num>/', user_detail),
    path('signup/', signup),
    path('profile/', profile),
]
