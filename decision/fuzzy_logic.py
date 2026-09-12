import numpy as np

class PriorityScorer:
    def __init__(self):
        # Placeholder for scikit-fuzzy implementation
        pass

    def compute_priority(self, distance, confidence):
        # Closer distance + higher confidence = higher priority
        priority = (100 - distance) * confidence
        return max(0, min(100, priority))\n