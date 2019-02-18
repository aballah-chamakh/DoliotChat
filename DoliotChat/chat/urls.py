from django.urls import path
from django.conf.urls  import include
from rest_framework import routers
from .views import ThreadViewSet

router = routers.DefaultRouter()
router.register('thread',ThreadViewSet)

urlpatterns = [
path('',include(router.urls))
]
