from line_follower_robot import sensor, movement

def main():
    try:
        
        sensor_values, active_count = sensor.get_sensor_data()
        
        
        if len(sensor_values) != 6:
            print("Error: Please enter exactly 6 sensor values.")
            return

        
        action = movement.decide_movement(sensor_values)
        
        
        print(f"\nSensor Values: {sensor_values}")
        print(f"Active Sensors: {active_count}")
        print(f"Robot Action: {action}")
        
    except ValueError:
        print("Error: Invalid input. Please enter only 0s and 1s.")

if __name__ == "__main__":
    main()