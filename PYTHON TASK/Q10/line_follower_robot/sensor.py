def get_sensor_data():
    user_input = input("Enter 6 sensor values (e.g., 001100): ")
    
    user_input = user_input.replace(" ", "")
    
    sensor_values = list(map(int, list(user_input)))
    
    active_sensors = len(list(filter(lambda x: x == 1, sensor_values)))
    
    return sensor_values, active_sensors