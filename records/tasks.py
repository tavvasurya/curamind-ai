from celery import shared_task
from .models import MedicalRecord
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import random
from django.conf import settings
from django.core.files import File


@shared_task
def process_medical_record(record_id):
    try:
        record = MedicalRecord.objects.get(id=record_id)
    except MedicalRecord.DoesNotExist:
        return "Record not found"

    try:
        image_path = record.file.path
        image = Image.open(image_path).convert("RGB")

        # Simulated AI Prediction
        disease_mapping = [
            "Normal",
            "Pneumonia",
            "Tuberculosis",
            "Lung Cancer",
            "Fracture"
        ]

        disease_name = random.choice(disease_mapping)

        # Generate Heatmap
        heatmap = np.random.rand(224, 224)
        heatmap = (heatmap * 255).astype("uint8")
        plt.figure(figsize=(6,6))
        plt.imshow(image.resize((224, 224)))
        plt.imshow(heatmap, cmap='jet', alpha=0.4)
        plt.colorbar(fraction=0.046, pad=0.04)
        plt.axis('off')
        

        heatmap_dir = os.path.join(settings.MEDIA_ROOT, "heatmaps")
        os.makedirs(heatmap_dir, exist_ok=True)

        heatmap_filename = f"heatmap_{record.id}.png"
        heatmap_full_path = os.path.join(heatmap_dir, heatmap_filename)

        plt.savefig(heatmap_full_path, bbox_inches='tight', pad_inches=0)
        plt.close()

        # Save correctly to ImageField
        with open(heatmap_full_path, "rb") as f:
            record.heatmap_image.save(heatmap_filename, File(f), save=False)

        record.ai_prediction = disease_name
        record.ai_processed = True
        record.save()

        return "AI Processing Completed"

    except Exception as e:
        return str(e)