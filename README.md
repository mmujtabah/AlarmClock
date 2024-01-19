# AlarmClock

## Overview
This is a simple Alarm Clock application built using PySide 6. It allows users to set alarms, and when the set time is reached, the application plays a sound to notify the user.

## Features
- Set multiple alarms with specific hours and minutes.
- Visual display of the current time.
- Remove alarms if they are no longer needed.
- Stop the alarm sound manually using the provided stop button.

## Prerequisites
- Python 3.11
- PySide 6
- pygame library (for playing sound)

## Installation
1. Clone the repository:
   ```git clone https://github.com/mmujtabah/AlarmClock.git```
2. Install dependencies:
  ```pip install -r requirements.txt```
3. Run the application:
   ```python widget.py```

## Usage
1. Launch the application.
2. Set alarms using the provided controls (hour and minute dropdowns, Set button).
3. Remove alarms if needed (Remove button).
4. Stop the alarm sound manually (Stop button).

## Strucuture
- ** widget.py: Main application file.
- ** ui_form.ui: PySide 6 UI file.
- ** ui_form.py: Auto-generated Python file from ui_form.ui.
- ** sound.mp3: Alarm sound file.
- ** alarm-clock.png: Application icon.

## Screenshots
![Screenshot 2024-01-10 203209](https://github.com/mmujtabah/AlarmClock/assets/64016614/c44fdd0b-da4a-4d10-a8de-212a80c30a9e)

## License
This project is licensed under the [MIT License](LICENSE).
