from django.utils.decorators import method_decorator
from rest_framework import viewsets, permissions
from .filters import MedicalDocFilterBackend, TreatmentFilterBackend
from .models import Patient, Treatment, MedicalDoc
from .serializers import PatientSerializer, TreatmentSerializer, MedicalDocSerializer, \
    TreatmentDetailSerializer, MedicalDocDetailSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


patient_param = openapi.Parameter('patient', openapi.IN_QUERY, description="Filter patient",
                                  type=openapi.TYPE_STRING)
treatment_param = openapi.Parameter('treatment', openapi.IN_QUERY, description="Filter treatment",
                                    type=openapi.TYPE_INTEGER)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']


@method_decorator(swagger_auto_schema(manual_parameters=[patient_param, treatment_param]),
                  name='list')
class MedicalDocViewSet(viewsets.ModelViewSet):
    queryset = MedicalDoc.objects.all()
    serializer_class = MedicalDocSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']
    filter_backends = [MedicalDocFilterBackend]

    def get_serializer_class(self):
        if self.action in ['retrieve', 'create']:
            return MedicalDocDetailSerializer
        return MedicalDocSerializer


@method_decorator(swagger_auto_schema(manual_parameters=[patient_param]), name='list')
class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']
    filter_backends = [TreatmentFilterBackend]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TreatmentDetailSerializer
        return TreatmentSerializer
