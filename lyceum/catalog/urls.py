from django.urls import path
from .views import item_list, item_detail

urlpatterns = [
    path('', item_list),
    path('<int:item_num>/', item_detail),
]