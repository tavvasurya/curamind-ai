from django.urls import path
from .views import (
    MedicalRecordCreateView,
    MedicalRecordListView,
    AppointmentCreateView,
    AppointmentListView,
    ai_status_view
)

urlpatterns = [
    # Medical Records
    path('upload/', MedicalRecordCreateView.as_view(), name='upload-record'),
    path('records/', MedicalRecordListView.as_view(), name='list-records'),

    # AI Status
    path('ai-status/<int:record_id>/', ai_status_view, name='ai-status'),

    # Appointments
    path('appointments/create/', AppointmentCreateView.as_view(), name='create-appointment'),
    path('appointments/', AppointmentListView.as_view(), name='list-appointments'),
]