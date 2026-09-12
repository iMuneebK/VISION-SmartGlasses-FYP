import time
from detection.yolo_detector import YoloDetector
from decision.fuzzy_logic import PriorityScorer
from sensors.ultrasonic import UltrasonicSensor
from alerts.tts_engine import TTSEngine

def main():
    print("Initializing VISION Smart Glasses Pipeline...")
    detector = YoloDetector()
    scorer = PriorityScorer()
    sensor = UltrasonicSensor()
    tts = TTSEngine()

    print("System Ready. Starting inference loop...")
    try:
        for _ in range(5):
            # 1. Capture object (mock)
            obj, conf = detector.detect()
            # 2. Get distance
            distance = sensor.get_distance()
            # 3. Calculate priority
            urgency = scorer.compute_priority(distance, conf)
            # 4. Alert user
            if urgency > 50:
                alert_msg = f"Warning: {obj} ahead at {distance} centimeters."
                print(f"[URGENT] {alert_msg}")
                tts.speak(alert_msg)
            else:
                print(f"[INFO] {obj} detected, but safe.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("System shutting down.")

if __name__ == "__main__":
    main()\n