from rest_framework import viewsets, permissions
from .models import Patient, Treatment, MedicalDoc, BodyDoc
from .serializers import PatientSerializer, TreatmentSerializer, MedicalDocSerializer
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


class MedicalDocViewSet(viewsets.ModelViewSet):
    queryset = MedicalDoc.objects.all()
    serializer_class = MedicalDocSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = self.queryset
        filter_patient = self.request.query_params.get('patient')
        fileter_treatment = self.request.query_params.get('treatment')
        if filter_patient:
            queryset = queryset.filter(patient__fio__icontains=filter_patient)
        if fileter_treatment:
            queryset = queryset.filter(treatment=fileter_treatment)
        return queryset

    @swagger_auto_schema(manual_parameters=[patient_param, treatment_param])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = self.queryset
        filter_patient = self.request.query_params.get('patient')
        if filter_patient:
            queryset = queryset.filter(patient__fio__icontains=filter_patient)
        return queryset

    @swagger_auto_schema(manual_parameters=[patient_param])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
