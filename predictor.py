import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.features = nn.Sequential(
            self._block(3, 32), self._block(32, 64),
            self._block(64, 128), self._block(128, 256)
        )
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.classifier = nn.Sequential(
            nn.Flatten(), nn.Dropout(0.4), nn.Linear(256, 2)
        )

    def _block(self, in_c, out_c):
        return nn.Sequential(
            nn.Conv2d(in_c, out_c, 3, padding=1),
            nn.BatchNorm2d(out_c), nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        return self.classifier(x)

class FreshnessPredictor:
    def __init__(self, model_type, weight_path, device):
        self.device = device
        self.model = SimpleCNN() if model_type == "Simple CNN" else self._get_resnet50()
        self.model.load_state_dict(torch.load(weight_path, map_location=device))
        self.model.to(device).eval()

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def _get_resnet50(self):
        model = models.resnet50(weights=None)
        model.fc = nn.Linear(model.fc.in_features, 2)
        return model

    def predict(self, input_data):
        """Handles both a single PIL image or a list of PIL images."""
        if not isinstance(input_data, list):
            input_data = [input_data]
            
        tensors = [self.transform(img) for img in input_data]
        batch_tensor = torch.stack(tensors).to(self.device)
        
        with torch.no_grad():
            outputs = self.model(batch_tensor)
            _, predicted = outputs.max(1)
            
        results = ["Fresh" if p.item() == 0 else "Spoiled" for p in predicted]
        return results