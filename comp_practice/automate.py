import pyautogui
import time

# Delay to give you time to focus on the input field
time.sleep(7)  # Adjust this to give you enough time to prepare

# The text to type
base_name = "30ter_c"

# Loop from 1 to 100
for i in range(35, 101):
    # Format the number as two digits (01, 02, ..., 100)
    text = f"{base_name}{i:02}"
    pyautogui.typewrite(text)  # Simulate typing
    pyautogui.press("enter")  # Simulate pressing the Enter key after each name
    time.sleep(0.9)  # Small delay to make it look more natural (optional)
