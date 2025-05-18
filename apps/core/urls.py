from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Crear router y registrar nuestros viewsets
router = DefaultRouter()
router.register('users', UserViewSet)

# Las URLs de la API son creadas automáticamente por el router
urlpatterns = router.urls
