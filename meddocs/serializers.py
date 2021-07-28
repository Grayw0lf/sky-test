from rest_framework import serializers
from .models import Patient, Treatment, MedicalDoc, BodyDoc


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class TreatmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Treatment
        fields = '__all__'


class MedicalDocSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    treatment = TreatmentSerializer

    class Meta:
        model = MedicalDoc
        fields = '__all__'


class BodyDocSerializer(serializers.ModelSerializer):
    medicaldoc = MedicalDocSerializer()

    class Meta:
        model = BodyDoc
        fields = '__all__'


class BodyDocNotDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyDoc
        fields = '__all__'


class MedicalDocDetailSerializer(MedicalDocSerializer):
    body = BodyDocNotDetailSerializer(source='bodydoc')

    class Meta:
        model = MedicalDoc
        fields = '__all__'


class TreatmentDetailSerializer(TreatmentSerializer):
    docs = MedicalDocSerializer(many=True, source='medicaldocs')

    class Meta:
        model = Treatment
        fields = '__all__'


