from django.urls import path
from .views import description

urlpatterns = [
    path('', description),
]
