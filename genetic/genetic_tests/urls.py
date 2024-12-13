from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeneticTestViewSet

router = DefaultRouter()
router.register(r'tests', GeneticTestViewSet, basename='genetic-test')

urlpatterns = [
    path('', include(router.urls)),
    path('statistics/', GeneticTestViewSet.as_view({'get': 'statistics'}), name='statistics'),
] 