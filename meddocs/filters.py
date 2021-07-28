from rest_framework.filters import BaseFilterBackend


class MedicalDocFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        filter_patient = request.query_params.get('patient')
        filter_treatment = request.query_params.get('treatment')
        if filter_patient:
            queryset = queryset.filter(patient__fio__icontains=filter_patient)
        if filter_treatment:
            queryset = queryset.filter(treatment=filter_treatment)
        return queryset


class TreatmentFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        filter_patient = request.query_params.get('patient')
        if filter_patient:
            queryset = queryset.filter(patient__fio__icontains=filter_patient)
        return queryset
