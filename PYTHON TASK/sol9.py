detections = [
    {"object": "box", "confidence": 78, "mode": "infrared", "distance": 2.5},
    {"object": "human", "confidence": 95, "mode": "camera", "distance": 1.2},
    {"object": "ball", "confidence": 82, "mode": "ultrasonic", "distance": 3.0},
    {"object": "human", "confidence": 88, "mode": "camera", "distance": 0.8},
    {"object": "chair", "confidence": 70, "mode": "infrared", "distance": 2.8}
]

valid_human_detections = list(filter(
    lambda d: d["object"] == "human" and d["mode"] == "camera" and d["confidence"] > 85,
    detections
))

distances = list(map(lambda d: d["distance"], valid_human_detections))

def check_proximity_alerts(distance_list):
    for distance in distance_list:
        if distance < 1.0:
            print("ALERT: Human very close!")
        else:
            print("Human detected at safe distance")

print("Valid Human Detections:")
print(valid_human_detections)

print("\nDistances:")
print(distances)

print("\nSafety System Status:")
check_proximity_alerts(distances)