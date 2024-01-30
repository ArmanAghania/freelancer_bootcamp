from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
