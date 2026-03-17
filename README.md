# Game AFK'er

A Python script that simulates automatic character movement in a game to prevent AFK (Away From Keyboard) disconnection.

## Description

Game AFKer is a simple automation tool that simulates random keyboard presses to keep your game character moving while you're away. The script presses two random movement keys (`a`, `w`, `s`, `d`) with a small random delay in between, making the behavior less predictable. This behaviour is repeated every 5 minutes until the user exists the script.

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

3. Open the game window, making it into focus - the script will start pressing keys immediately every 5 seconds

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
