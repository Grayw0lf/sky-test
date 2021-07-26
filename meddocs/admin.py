from django.contrib import admin
from .models import Patient, Treatment, MedicalDoc, BodyDoc


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    pass


@admin.register(MedicalDoc)
class MedicalDocAdmin(admin.ModelAdmin):
    pass

@admin.register(BodyDoc)
class BodyDocAdmin(admin.ModelAdmin):
    pass
