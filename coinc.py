import pyautogui
import pyscreeze
import time
import random
import cv2
import numpy as np

# Disable exceptions for image not found
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

# Dapatkan ukuran layar penuh secara otomatis
screen_width, screen_height = pyautogui.size()

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
    location = retry_find_image("img/chrome.png")
    if location:
        pyautogui.click(location)
    else:
        backhome()

def select_coincather():
    location = retry_find_image("img/coinclick.png", confidence=0.8)
    if location:
        pyautogui.click(location[0], location[1] + 50)
    else:
        backhome()

def start():
    print("Searching for the 'Start' button...")
    location = retry_find_image("img/start.png")
    if location:
        pyautogui.click(location)
        print("Start button clicked.")
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

def click_on_RGBpixel(r_value, g_value, b_value, coords):
    pic = pyautogui.screenshot(region=coords)
    for x in range(0, coords[2], 6):
        for y in range(0, coords[3], 6):
            r, g, b = pic.getpixel((x, y))
            if r == r_value and g == g_value and b == b_value:
                pyautogui.click(x + coords[0], y + coords[1])
                return True
    return False

def play():
    print("Starting play function...")
    scan_region = (428, 171, 1497, 800)  # Define the region you want to scan
    values = [(171, 143, 52), (0, 96, 158), (91, 128, 231), (110, 139, 214), (191, 191, 191), (255, 153, 51)]  # Coin colors

    while True:
        # Check for victory every second
        if victory_check():
            print("Victory detected! Exiting play function.")
            break

        scan = pyautogui.screenshot()
        rgb_check = scan.getpixel((338, 48))

        if all(scan.getpixel((338, 48)) == rgb_check for _ in range(5)):
            for value in values:
                if click_on_RGBpixel(value[0], value[1], value[2], scan_region):
                    print(f"Clicked on color {value}")
                    break
        time.sleep(0.01)  # Avoid checking too rapidly

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
    select_coincather()
    time.sleep(4)
    start()
    time.sleep(5)
    play()  # Will run for up to 50 seconds
    time.sleep(7)
    gain()
    backtogames()
