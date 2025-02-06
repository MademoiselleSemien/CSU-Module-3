# Alarm Clock Calculator (24-hour format)

# Get the current time from the user
current_time = int(input("Enter the current time (0-23): "))

# Get the number of hours to wait
wait_time = int(input("Enter the number of hours to wait for the alarm: "))

# Calculate the alarm time
alarm_time = (current_time + wait_time) % 24

# Display the result
print(f"The alarm will go off at {alarm_time}:00.")
