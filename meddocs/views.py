from rest_framework import viewsets, permissions
from .models import Patient, Treatment, MedicalDoc, BodyDoc
from .serializers import PatientSerializer, TreatmentSerializer, MedicalDocSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = self.queryset
        filter_fio = self.request.query_params.get('fio')
        if filter_fio:
            queryset = queryset.filter(fio__contains=filter_fio)
        return queryset


class MedicalDocViewSet(viewsets.ModelViewSet):
    queryset = MedicalDoc.objects.all()
    serializer_class = MedicalDocSerializer
    permission_classes = [permissions.AllowAny]


class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [permissions.AllowAny]
