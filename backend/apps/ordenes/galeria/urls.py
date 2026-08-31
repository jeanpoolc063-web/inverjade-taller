from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FotoOrdenViewSet

router = DefaultRouter()
router.register(r'', FotoOrdenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
