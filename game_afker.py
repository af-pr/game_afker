import pyautogui
import time
import random
import signal
import sys
from apscheduler.schedulers.background import BackgroundScheduler

# CONFIGURATION
movement_interval_min = 60                        # Minimum time in seconds between pairs of movements
movement_interval_max = movement_interval_min + 30  # Maximum time in seconds between pairs of movements
press_time_min = 0.5                                # Minimum time to hold down a key in seconds
press_time_max = 0.8                                # Maximum time to hold down a key in seconds

#Other global variables
execution_count = 0                     # Counter for number of executions. Do not modifity
direction_keys = ['a', 'w', 's', 'd']   # Possible movement keys
opposite_keys = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}

# Restricted mode state
allowed_keys = []                       # Allowed keys for restricted mode
pending_return_key = None               # Key to press on the return (B) cycle
pending_return_duration = None          # Duration to hold the return key


def press_key(key: str, duration: float):
    """
    Press a key for a specified duration.

    Args:
        key (str): The key to press (e.g., 'a', 'w', 's', 'd').
        duration (float): The time in seconds to hold the key down.
    """
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)
    
def simulate_restricted_movement():
    """
    Simulate restricted movement in A/B cycles.
    A: Press a random allowed key once, store opposite key and duration.
    B: Press the stored opposite key with the same duration.
    """
    global execution_count, pending_return_key, pending_return_duration
    execution_count += 1

    if pending_return_key:
        key = pending_return_key
        duration = pending_return_duration
        pending_return_key = None
        pending_return_duration = None
        print(f"\nExecuting restricted movement (Execution #{execution_count}) - Return: {key.upper()}")
    else:
        key = random.choice(allowed_keys)
        duration = random.uniform(press_time_min, press_time_max)
        pending_return_key = opposite_keys[key]
        pending_return_duration = duration
        print(f"\nExecuting restricted movement (Execution #{execution_count}) - Move: {key.upper()}")

    press_key(key, duration)

def simulate_default_movement(pause_min=0.5, pause_max=1.0):
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
    press_key(key1, random.uniform(press_time_min, press_time_max))  # Random sleep between 0.2 and 0.7 seconds
    # Pause between moves
    time.sleep(random.uniform(pause_min, pause_max))
    # Press 2nd key
    press_key(key2, random.uniform(press_time_min, press_time_max))  # Random sleep between 0.2 and 0.7 seconds


def schedule_default_movement():
    simulate_default_movement()
    # Reschedule with random interval
    scheduler.reschedule_job('movement', trigger='interval', seconds=random.uniform(movement_interval_min, movement_interval_max))

def schedule_restricted_movement():
    simulate_restricted_movement()
    scheduler.reschedule_job('movement', trigger='interval', seconds=random.uniform(movement_interval_min, movement_interval_max))

def signal_handler(sig, frame):
    scheduler.shutdown(wait=False)
    print("\nScript stopped by user. Not pressing any keys anymore.")
    sys.exit(0)
    
def select_mode():
    """Ask the user for operating mode and configure the scheduler job accordingly."""
    global allowed_keys
    mode = input("\nSelect mode ((f) free / (r) restricted) [default: free]: ").strip().lower()

    if mode in ('r', 'restricted'):
        while True:
            raw = input("Allowed directions (combination of w/a/s/d): ").strip().lower()
            allowed_keys = sorted({ch for ch in raw if ch in direction_keys})
            if allowed_keys:
                print(f"Directions set: {', '.join(k.upper() for k in allowed_keys)}")
                return schedule_restricted_movement
            print("Provide at least one valid direction (w, a, s, d).")
    else:
        return schedule_default_movement


# ------------------------#
#       MAIN SCRIPT       #
# ------------------------#

signal.signal(signal.SIGINT, signal_handler)

movement_job = select_mode()
scheduler = BackgroundScheduler()
scheduler.add_job(movement_job, 'interval', seconds=movement_interval_min, id='movement')

print("\nStarting movement simulation...")
scheduler.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
