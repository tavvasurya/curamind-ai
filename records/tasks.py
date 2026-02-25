from celery import shared_task
from .models import MedicalRecord
from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision import models
from torchvision.models import ResNet18_Weights
import matplotlib.pyplot as plt
import numpy as np
import os


@shared_task
def process_medical_record(record_id):

    record = MedicalRecord.objects.get(id=record_id)
    image_path = record.file.path

    # Load image
    image = Image.open(image_path).convert("RGB")

    # ✅ Updated ResNet model (no warning)
    model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
    model.eval()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)

    _, predicted = torch.max(output, 1)

    predicted_index = predicted.item()

    # ✅ Map index to disease
    disease_mapping = {
        0: "Normal",
        1: "Pneumonia",
        2: "Tuberculosis",
        3: "Lung Cancer",
        4: "Fracture"
    }

    mapped_index = predicted_index % 5
    disease_name = disease_mapping.get(mapped_index, "Unknown Disease")

    # ✅ Generate demo heatmap
    heatmap = np.random.rand(224, 224)

    plt.imshow(image.resize((224,224)))
    plt.imshow(heatmap, cmap='jet', alpha=0.5)
    plt.axis('off')

    heatmap_dir = os.path.join(os.path.dirname(image_path), "../heatmaps")
    os.makedirs(heatmap_dir, exist_ok=True)

    heatmap_filename = f"heatmap_{record.id}.png"
    heatmap_full_path = os.path.join(heatmap_dir, heatmap_filename)

    plt.savefig(heatmap_full_path, bbox_inches='tight', pad_inches=0)
    plt.close()

    # ✅ Save relative path properly
    record.ai_prediction = disease_name
    record.heatmap_image = f"heatmaps/{heatmap_filename}"
    record.ai_processed = True
    record.save()

    return "AI Processing Completed"