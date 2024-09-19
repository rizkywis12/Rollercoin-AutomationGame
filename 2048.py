import pyautogui
import pyscreeze
import time
import random

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

def retry_find_image(image_path, retries=5, interval=2, confidence=0.9):
    """Coba mencari gambar dengan retry sebanyak retries kali dan delay antar percobaan interval detik."""
    for attempt in range(retries):
        print(f"Attempt {attempt + 1} to find {image_path}...")
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location is not None:
            print(f"Image {image_path} found!")
            return location
        print(f"Image {image_path} not found. Retrying in {interval} seconds...")
        time.sleep(interval)
    print(f"Failed to find {image_path} after {retries} attempts.")
    return None

def backhome():
    """Klik pada gambar backhome.png untuk kembali ke halaman utama."""
    print("Clicking backhome.png to return to the home page.")
    location = retry_find_image("img/backhome.png")
    if location:
        pyautogui.click(location)
    else:
        print("Failed to click backhome.png, image not found.")

def chrome_open():
    x, y = retry_find_image("img/chrome.png")
    if x and y:
        pyautogui.click(x, y)
        screen_width, screen_height = pyautogui.size()
        pyautogui.moveTo(screen_width / 2, screen_height / 2)
        time.sleep(1)
        pyautogui.scroll(-500)
        time.sleep(1)
    else:
        backhome()

def select_2048():
    location = retry_find_image("img/2048.png")
    if location:
        pyautogui.click(location[0], location[1] + 40)
    else:
        backhome()

def start():
    location = retry_find_image("img/start2.png")
    if location:
        pyautogui.click(location)
    else:
        backhome()

def gain():
    location = retry_find_image("img/gain.png")
    if location:
        pyautogui.click(location)
    else:
        print("Gain image not found after retries.")
        backhome()

def backtogames():
    print("Waiting for 'Back to Games' image to appear...")
    location = retry_find_image("img/backtogames.png")
    if location:
        pyautogui.click(location)
        print("Clicked 'Back to Games'.")
    else:
        print("'Back to Games' image not found. Returning home...")
        backhome()

def play():
    print("Starting play function...")
    pixel = pyautogui.pixel(900, 533)
    initial_position = pyautogui.position()

    while True:
        if victory_check():
            print("Victory detected! Exiting play function.")
            break

        direction = random.choice(['down', 'up', 'left', 'right'])
        x, y = pyautogui.position()

        if direction == 'down':
            print("Dragging down...")
            pyautogui.dragTo(x, y + 200, duration=0.3)
        elif direction == 'up':
            print("Dragging up...")
            pyautogui.dragTo(x, y - 200, duration=0.3)
        elif direction == 'left':
            print("Dragging left...")
            pyautogui.dragTo(x - 200, y, duration=0.3)
        elif direction == 'right':
            print("Dragging right...")
            pyautogui.dragTo(x + 200, y, duration=0.3)

        pyautogui.moveTo(initial_position)
        time.sleep(0.01)

def victory_check():
    print("Checking for victory...")
    location = pyautogui.locateCenterOnScreen("img/victory.png", confidence=0.9)
    if location is not None:
        print("Victory detected!")
        return True
    return False

if __name__ == "__main__":
    chrome_open()
    time.sleep(1)
    select_2048()
    time.sleep(4)
    start()
    time.sleep(5)
    play()
    time.sleep(7)
    gain()
    backtogames()
