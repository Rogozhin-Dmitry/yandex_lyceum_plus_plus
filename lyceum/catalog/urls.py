from django.urls import path

from .views import estimate_item, item_detail, item_list

urlpatterns = [
    path("", item_list),
    path("<int:item_num>/", item_detail),
    path("<int:item_num>/estimate", estimate_item),
]
