from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewset,ProfileViewSet

router  = routers.DefaultRouter()
router.register('user',UserViewset)
router.register('profile',ProfileViewSet)

urlpatterns = [
path('',include(router.urls)),

]
