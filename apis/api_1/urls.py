from django.urls import path, include
from rest_framework import routers

from .views import ApiViewSet

app_name = 'api_1'

router = routers.SimpleRouter()
router.register('', ApiViewSet, basename='api_1')

urlpatterns = [
    path('', include(router.urls)),
]