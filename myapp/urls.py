from rest_framework import routers
from django.urls import path
from .api import ProjectViewSet
from .views import LatestSensorDataView

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet,'projects')
urlpatterns = [
    *router.urls,
    path('api/latest-sensor-data/', LatestSensorDataView.as_view(), name='latest-sensor-data'),
]