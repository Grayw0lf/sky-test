from django.urls import path, include
from rest_framework import routers
from .views import PatientViewSet, TreatmentViewSet, MedicalDocViewSet


router = routers.DefaultRouter()
router.register('patients', PatientViewSet)
router.register('treatments', TreatmentViewSet)
router.register('medical-docs', MedicalDocViewSet)


urlpatterns = [
    path('', include(router.urls)),
]