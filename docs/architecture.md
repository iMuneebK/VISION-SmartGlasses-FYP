# System Architecture

The VISION system follows a strict real-time pipeline:
1. **Sensor Fusion**: Camera captures frames, Ultrasonic measures depth.
2. **Perception**: YOLOv8 extracts bounding boxes and object classes.
3. **Decision Making**: Fuzzy Logic system scores obstacles based on class threat, distance, and approach velocity.
4. **Feedback**: Text-to-Speech engine delivers localized audio cues.\n