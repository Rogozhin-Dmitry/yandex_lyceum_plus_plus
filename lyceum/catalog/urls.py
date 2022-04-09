from django.urls import path

from .views import item_detail, item_list

urlpatterns = [
    path("", item_list),
    path("<int:item_num>/", item_detail),
]
