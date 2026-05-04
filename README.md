# win-shift-back

Overview

This repository provides a reusable Python function to trigger the Win + Shift + Backspace keyboard shortcut using automation.

It is designed to be part of a larger automation framework for interacting with Remote Incident Manager (RIM) sessions, specifically for opening the session menu reliably.

⚙️ Features
Presses Win + Shift + Backspace using pyautogui
Returns structured results:
PASS
FAIL

Follows a consistent automation result format:

{
    "status": "PASS / FAIL",
    "message": ""
}
📦 Project Structure
win_shift_back/
│
├── __init__.py
├── actions.py
🚀 Installation (Local Use)

Clone the repository:

git clone https://github.com/YOUR_USERNAME/win-shift-back.git

Navigate into your project and ensure the folder is named:

win_shift_back
🧠 Usage
from win_shift_back import press_win_shift_back

result = press_win_shift_back()
print(result)
🧪 Example Output
{
    "status": "PASS",
    "message": "Win + Shift + Backspace was pressed successfully."
}
⚠️ Requirements
Python 3.x
pyautogui

Install dependency:

pip install pyautogui
⚠️ Important Notes
The target window must be in focus for the shortcut to work.
This function does not validate UI changes — it only performs the key press.
Intended to be combined with additional validation functions using tools like pywinauto.
🧱 Future Improvements
Add validation to confirm menu opening
Integrate with UI-based actions (e.g., clicking "Flip Session")
Expand into a full automation module
🧠 Design Philosophy

This project follows a structured automation approach:

Action functions → perform interactions
Validation functions → verify results
Result format → consistent PASS/FAIL structure
