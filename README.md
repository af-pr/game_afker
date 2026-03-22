# Game AFK'er

A Python script that simulates automatic character movement in a game to prevent AFK (Away From Keyboard) disconnection.

## Description

Game AFKer is a simple automation tool that simulates character movement in a game to prevent AFK (Away From Keyboard) disconnection. It offers two operating modes:

- **Free Mode (default):** Simulates random keyboard presses with two random movement keys (`a`, `w`, `s`, `d`) with a small random delay in between, making the behavior unpredictable.
- **Restricted Mode:** Allows you to specify allowed movement directions. The script alternates into two-cycle pairs:
  - **Cycle A:** Presses one random key from your allowed directions
  - **Cycle B:** Presses the opposite direction (w↔s, a↔d) with the exact same duration as Cycle A
  
Both modes repeat every 5 minutes (with random variance) until you exit the script.

## Prerequisites

- Python 3.7 or higher
- Windows (due to `pyautogui` usage)

## Installation

1. **Clone or download the project:**
   ```
   https://github.com/af-pr/game_afker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the script

1. Open a terminal in the project folder. Running the terminal as an administrator might be necessary depending on the game.
2. Run the script:
   ```bash
   python game_afker.py
   ```

3. Select your operating mode:
   - Press `1` or `Enter` for **Free Mode** (default)
   - Press `2` (or type `r`/`restricted`) for **Restricted Mode**

4. If you choose **Restricted Mode**, enter the allowed movement directions:
   - Type any combination of `w`, `a`, `s`, `d` (e.g., `wa`, `sad`, `wasd`)
   - Duplicates and invalid characters are automatically ignored
   - At least one valid direction is required

5. Open the game window, making it into focus - the script will start pressing keys immediately

### Mode Details

**Free Mode:**
- Presses two random directions per cycle
- Repeats every ~5 minutes

**Restricted Mode:**
- Cycle A: Presses a random key from your allowed directions
- Cycle B: Presses the opposite direction with the same duration
- Pattern repeats: A → B → A → B → ...
- Repeats every ~5 minutes

### Stopping execution

There are two ways to stop the script:

- **Option 1 - Keyboard interrupt:**
  - Press `Ctrl + C` in the terminal where the script is running
  - You'll see the message: `Script stopped by user. Not pressing any keys anymore.`

- **Option 2 - Close the terminal:**
  - Close the terminal window directly

## Custom configuration

You can adjust the parameters at the top of the `game_afker.py` file:

```python
movement_interval_min = 5*60    # Minimum time in seconds between pairs of movements
movement_interval_max = 6*60    # Maximum time in seconds between pairs of movements
press_time_min = 0.2            # Minimum time to hold down a key in seconds
press_time_max = 0.5            # Maximum time to hold down a key in seconds
```

## Troubleshooting

### The script runs but the character doesn't move

1. **Verify the script is running** there should be a log in the terminal similar to "Executing movement simulation (Execution #1) - Keys: D, S" each time the movements are being tried
2. **Make sure the game is in focus** when the movements are being tried
3. **Check if the keys are being pressed** - you can set the focus to another program to check if the keys are being pressed. For example you can open notepad and check if some of the random key letters are being written. You might want to adjust movement_interval and check_interval to avoid long waiting.
4. **Run as administrator** - some games require elevated permissions:
   - Right-click on PowerShell → "Run as administrator"
   - Then run the script

### The script doesn't start correctly

- Verify that dependencies are installed: `pip list`
- Try reinstalling: `pip install --upgrade -r requirements.txt`

## Project files

- `game_afker.py` - Main script
- `requirements.txt` - Project dependencies
- `README.md` - This file

## Important notes

⚠️ **Disclaimer:** This script is designed for personal use in games that allow it. Some games may consider bots as a violation of their terms of service. Use it at your own risk.

## License

[MIT](LICENSE)

## Author

Created by af-pr - https://github.com/af-pr
