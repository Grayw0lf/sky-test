from django.urls import path, include
from rest_framework import routers
from .views import PatientViewSet, TreatmentViewSet


router = routers.DefaultRouter()
router.register('patients', PatientViewSet)
router.register('treatments', TreatmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]