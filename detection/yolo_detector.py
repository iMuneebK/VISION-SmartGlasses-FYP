import random
class YoloDetector:
    def __init__(self):
        self.classes = ['car', 'person', 'bicycle', 'stop sign', 'staircase']
    def detect(self):
        # In real implementation: model.predict(frame)
        return random.choice(self.classes), random.uniform(0.6, 0.99)\n