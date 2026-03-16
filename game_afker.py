import pyautogui
import schedule
import time
import random

# CONFIGURATION
movement_interval = 5*60        # Scheduled time interval in seconds for each movement group execution
movement_interval_range = 20    # Maximum variation seconds to add to the movement interval for randomness (0 to movement_interval_range seconds)
check_interval = 60             # Time interval in seconds to check for pending scheduled tasks. Adjust as needed.
press_time_min = 0.2            # Minimum time to hold down a key in seconds
press_time_max = 0.5            # Maximum time to hold down a key in seconds

execution_count = 0                     # Counter for number of executions. Do not modifity
direction_keys = ['a', 'w', 's', 'd']   # Possible movement keys

def simulate_movement(pause_min=0.5, pause_max=1.0):
    """
    Simulate keyboard movement with two moves with random direction.
    Randomly selects two keys from a, w, s, d to press.

    Args:       pause_min (float): The minimum time to wait between key presses in seconds. Default is 0.5 seconds.
                pause_max (float): The maximum time to wait between key presses in seconds. Default is 1.0 seconds.
    Returns:     None
    """
    global execution_count
    execution_count += 1
    
    # Select two random keys
    key1 = random.choice(direction_keys)
    key2 = random.choice(direction_keys)
    
    print(f"\nExecuting movement simulation (Execution #{execution_count}) - Keys: {key1.upper()}, {key2.upper()}")
    
    # Press 1st key
    pyautogui.keyDown(key1)
    time.sleep(random.uniform(press_time_min, press_time_max))  # Random sleep between 0.2 and 0.7 seconds
    pyautogui.keyUp(key1)
    # Pause between moves
    time.sleep(random.uniform(pause_min, pause_max))
    # Press 2nd key
    pyautogui.keyDown(key2)
    time.sleep(random.uniform(press_time_min, press_time_max))  # Random sleep between 0.2 and 0.7 seconds
    pyautogui.keyUp(key2)


# ------------------------#
#       MAIN SCRIPT       #
# ------------------------#
schedule.every(movement_interval).seconds.do(simulate_movement)

print("\nStarting movement simulation...")
try:
    while True:
        schedule.run_pending()
        time.sleep(check_interval)
except KeyboardInterrupt:
    print("\nScript stopped by user. Not pressing any keys anymore.")
