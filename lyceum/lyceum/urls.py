from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("auth/", include("users.urls")),
    path("rating/", include("rating.urls")),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]
