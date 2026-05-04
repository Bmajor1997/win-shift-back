import pyautogui
import time


def press_win_shift_back():

    result = {
        "status": None,
        "message": ""
    }

    try:
        time.sleep(2)

        pyautogui.hotkey('winleft', 'shift', 'backspace')

        time.sleep(1)

        result["status"] = "PASS"
        result["message"] = "Win + Shift + Backspace was pressed successfully."

        return result

    except Exception as e:
        result["status"] = "FAIL"
        result["message"] = str(e)

        return result
