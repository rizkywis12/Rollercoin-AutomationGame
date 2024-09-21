import pyautogui

x, y = pyautogui.position()  # Get current mouse position
color = pyautogui.pixel(x, y)  # Get color of the pixel under the mouse
print(f"Position: ({x}, {y}), Color: {color}")
