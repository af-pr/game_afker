import pyautogui
import time
import random
import signal
import sys
from apscheduler.schedulers.background import BackgroundScheduler

# CONFIGURATION
movement_interval_min = 60                        # Minimum time in seconds between pairs of movements
movement_interval_max = movement_interval_min + 30  # Maximum time in seconds between pairs of movements
press_time_min = 0.2                                # Minimum time to hold down a key in seconds
press_time_max = 0.5                                # Maximum time to hold down a key in seconds

#Other global variables
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


def scheduled_movement():
    simulate_movement()
    # Reschedule with random interval
    scheduler.reschedule_job('movement', trigger='interval', seconds=random.uniform(movement_interval_min, movement_interval_max))

def signal_handler(sig, frame):
    scheduler.shutdown(wait=False)
    print("\nScript stopped by user. Not pressing any keys anymore.")
    sys.exit(0)
    
# ------------------------#
#       MAIN SCRIPT       #
# ------------------------#

signal.signal(signal.SIGINT, signal_handler)

scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_movement, 'interval', seconds=movement_interval_min, id='movement')

print("\nStarting movement simulation...")
scheduler.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
