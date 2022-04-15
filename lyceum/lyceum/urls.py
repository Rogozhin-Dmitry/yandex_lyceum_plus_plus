from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("homepage.urls"), name='homepage'),
    path("catalog/", include("catalog.urls"), name='catalog'),
    path("about/", include("about.urls"), name='about'),
    path("auth/", include("users.urls"), name='users'),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]
