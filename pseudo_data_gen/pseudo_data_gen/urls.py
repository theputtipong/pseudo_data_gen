# myproject/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp import views

router = DefaultRouter()
router.register(r"mymodels", views.MyModelViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    # other paths
]
