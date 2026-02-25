from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Appointment, MedicalRecord
from .serializers import AppointmentSerializer, MedicalRecordSerializer
from .permissions import IsDoctor
from .tasks import process_medical_record


# ===============================
# Medical Record Upload (Doctor Only)
# ===============================
class MedicalRecordCreateView(generics.CreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        record = serializer.save(doctor=self.request.user)

        # 🔥 Trigger Celery AI Task
        process_medical_record.delay(record.id)


# ===============================
# Medical Record List (Role Based)
# ===============================
class MedicalRecordListView(generics.ListAPIView):
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'doctor':
            return MedicalRecord.objects.filter(doctor=user)

        elif user.role == 'patient':
            return MedicalRecord.objects.filter(patient=user)

        return MedicalRecord.objects.none()


# ===============================
# AI Status View
# ===============================
@api_view(['GET'])
def ai_status_view(request, record_id):
    try:
        record = MedicalRecord.objects.get(id=record_id)
    except MedicalRecord.DoesNotExist:
        return Response({"error": "Record not found"}, status=404)

    return Response({
        "ai_processed": record.ai_processed,
        "ai_prediction": record.ai_prediction,
        "heatmap_image": request.build_absolute_uri(record.heatmap_image.url) if record.heatmap_image else None
    })


# ===============================
# Appointment Create
# ===============================
class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role == 'doctor':
            serializer.save(doctor=self.request.user)
        else:
            serializer.save(patient=self.request.user)


# ===============================
# Appointment List
# ===============================
class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'doctor':
            return Appointment.objects.filter(doctor=user)

        elif user.role == 'patient':
            return Appointment.objects.filter(patient=user)

        return Appointment.objects.none()


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')