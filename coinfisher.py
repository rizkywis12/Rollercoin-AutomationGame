import pyautogui
import pyscreeze
import time
import random
import cv2
import numpy as np
import math

# Disable exceptions for image not found
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

# Dapatkan ukuran layar penuh secara otomatis
screen_width, screen_height = pyautogui.size()

def chrome_open():
    try:
        x, y = pyautogui.locateCenterOnScreen("img/chrome.png", confidence=0.9)
        pyautogui.click(x, y)
    except TypeError:
        print("Chrome icon not found.")

def select_coincather():
    try:
        x, y = pyautogui.locateCenterOnScreen("img/coinfisher.png", confidence=0.8)
        pyautogui.click(x, y + 40)
    except TypeError:
        print("Coin Catcher icon not found.")

def start():
    print("Searching for the 'Start' button...")
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("img/start2.png", confidence=0.9)
            pyautogui.click(x, y)
            print("Start button clicked.")
            break  # Exit the loop once the button is found and clicked
        except TypeError:
            print("Start button not found. Retrying...")
            time.sleep(1)  # Wait for 1 second before trying again

def gain():
    try:
        x, y = pyautogui.locateCenterOnScreen("img/gain.png", confidence=0.9)
        pyautogui.click(x, y)
    except TypeError:
        print("Gain image not found.")

def backtogames():
    print("Waiting for 'Back to Games' image to appear...")
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("img/backtogames.png", confidence=0.9)
            pyautogui.click(x, y)
            print("Clicked 'Back to Games'.")
            break  # Exit the loop after clicking
        except TypeError:
            print("Back to games image not found. Checking again...")
            time.sleep(1)  # Wait for 1 second before checking again

def click_on_RGBpixel(r_value, g_value, b_value, coords):
    pic = pyautogui.screenshot(region=coords)
    mouse_x, mouse_y = pyautogui.position()
    
    farthest_coin = None
    max_distance = 0

    # Search for all coins and calculate the farthest one
    for x in range(0, coords[2], 6):
        for y in range(0, coords[3], 6):
            r, g, b = pic.getpixel((x, y))
            if r == r_value and g == g_value and b == b_value:
                coin_x = x + coords[0]
                coin_y = y + coords[1]
                distance = math.sqrt((coin_x - mouse_x) ** 2 + (coin_y - mouse_y) ** 2)
                
                if distance > max_distance:
                    max_distance = distance
                    farthest_coin = (coin_x, coin_y)

    # Click on the farthest coin
    if farthest_coin:
        pyautogui.click(farthest_coin[0], farthest_coin[1])
        return True

    return False

def play():
    print("Starting play function...")
    scan_region = (205, 171, 1309, 838)  # Define the region you want to scan (ubah sesuai yang diinginkan)
    values = [(171, 143, 52), (0, 96, 158), (91, 128, 231), (110, 139, 214), (191, 191, 191), (255, 153, 51)]  # Replace with your coin colors

    # Randomly shuffle the colors to avoid spam-clicking in the same pattern
    random.shuffle(values)

    while True:
        # Check for victory every second
        if victory_check():
            print("Victory detected! Exiting play function.")
            break
        
        scan = pyautogui.screenshot()
        rgb_check = scan.getpixel((338, 48))
        
        if all(scan.getpixel((338, 48)) == rgb_check for _ in range(5)):
            # Iterate over colors in random order
            for value in values:
                if click_on_RGBpixel(value[0], value[1], value[2], scan_region):
                    print(f"Clicked on farthest color {value}")
                    
                    # Wait for a short, random time before searching again to avoid spamming
                    time.sleep(random.uniform(0.05, 0.3))
                    
                    # Shuffle colors again to randomize the next search
                    random.shuffle(values)
                    break
        time.sleep(0.03)  # Avoid checking too rapidly

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
    time.sleep(6)
    start()
    time.sleep(5)
    play()  # Will run for up to 50 seconds
    time.sleep(7)
    gain()
    backtogames()
