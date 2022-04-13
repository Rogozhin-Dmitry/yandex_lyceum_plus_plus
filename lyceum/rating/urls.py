from django.urls import path
from rating.views import new_rating_form

urlpatterns = [
    path("rate/<int:item_num>", new_rating_form),
]
