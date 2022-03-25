from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet

router = routers.DefaultRouter()
router.register(r"person", PersonViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
