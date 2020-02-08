from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router1 = routers.DefaultRouter()

router.register('api',views.DestinationView)
router.register('low',views.DestinationView)

# router1.register('low',views.DestinationView)

urlpatterns = [
    path("",views.index,name="index"),
    path("api/",include(router.urls)),
    # path("api/",include(router1.urls))

]