from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserVieset,ProfileViewSet

router  = routers.defaultRouter()
router.register('user',UserVieset)
router.register('profile',ProfileViewSet)

urlspatterns = [
path('',include(router.urls)),

]
