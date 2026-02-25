from rest_framework import serializers
from .models import Appointment, MedicalRecord


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['doctor', 'created_at']


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        read_only_fields = [
            'doctor',
            'uploaded_at',
            'ai_prediction',
            'heatmap_image',
            'ai_processed'
        ]