def decide_movement(sensors):
    left_sensors = sensors[:2]      # Indices 0, 1
    middle_sensors = sensors[2:4]   # Indices 2, 3
    right_sensors = sensors[4:]     # Indices 4, 5
    
    total_active = sum(sensors)
    
    if total_active == 0:
        return "Stop Robot"
        
    elif total_active == 6:
        return "Junction Detected"
        
    elif sum(left_sensors) > sum(right_sensors):
        return "Turn Left"
        
    elif sum(right_sensors) > sum(left_sensors):
        return "Turn Right"
        
    elif sum(middle_sensors) > 0:
        return "Move Forward"
        
    else:
        return "Unknown Action"