# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, CategoryViewSet, TransactionViewSet, UserViewSet

router = DefaultRouter()
router.register(r"accounts", AccountViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"transactions", TransactionViewSet)
router.register(r"users", UserViewSet)  # <-- Nuevo endpoint

urlpatterns = [
    path("", include(router.urls)),
]
