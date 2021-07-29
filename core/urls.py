from django.urls import path, include
from rest_framework import routers

from .views import SchedulingViewSet


router = routers.DefaultRouter()

router.register('scheduling', SchedulingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
