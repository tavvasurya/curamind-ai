from django.db import models
from django.conf import settings


# ===============================
# Appointment Model
# ===============================
class Appointment(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_appointments'
    )
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_appointments'
    )

    appointment_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('scheduled', 'Scheduled'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        default='scheduled'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} → {self.doctor.username} on {self.appointment_date}"


# ===============================
# Medical Record Model
# ===============================
class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='medical_records'
    )

    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='doctor_records'
    )

    diagnosis = models.TextField(blank=True, null=True)

    file = models.FileField(upload_to='medical_files/')

    # 🔥 Week 3 Fields
    ai_prediction = models.CharField(max_length=255, blank=True, null=True)
    heatmap_image = models.ImageField(upload_to='heatmaps/', blank=True, null=True)
    ai_processed = models.BooleanField(default=False)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record for {self.patient.username}"