from django.urls import path

from .views import item_list, ItemDetail

urlpatterns = [
    path("", item_list, name='item_list'),
    path("<int:item_num>/", ItemDetail.as_view(), name='item_detail'),
]
