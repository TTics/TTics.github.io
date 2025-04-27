river_speed = 25
time = 0  # Total time in hours

while river_speed > 10:
    pebble_speed = river_speed * 0.6  # Pebble speed depends on river speed
    traveled_distance = pebble_speed  # Distance traveled in this hour
    time += 1  # Each iteration represents 1 hour passing
    river_speed -= pebble_speed * 0.5  # River slows down

# Calculate any additional fractional time for the last partial hour
if river_speed + (pebble_speed * 0.5) > 10:  # Check if it was close to finishing
    remaining_distance = 10 - river_speed  # Remaining distance before slowing stops
    pebble_speed = river_speed * 0.6
    fractional_time = remaining_distance / pebble_speed  # Time for the last part
    time += fractional_time

# Convert time to hours and minutes for display
hours = int(time)
minutes = (time - hours) * 60

print(f"{hours} hours and {minutes:.2f} minutes")
