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

# Warna bola yang akan diikuti (RGB)
BALL_COLOR = (162, 192, 197)

# Fungsi untuk membuka Chrome
def chrome_open():
    try:
        x, y = pyautogui.locateCenterOnScreen("img/chrome.png", confidence=0.9)
        pyautogui.click(x, y)
    except TypeError:
        print("Chrome icon not found.")

# Fungsi untuk memilih game Coin Catcher
def select_coincatcher():
    try:
        x, y = pyautogui.locateCenterOnScreen("img/cryptonoid.png", confidence=0.9)
        pyautogui.click(x, y + 30)
    except TypeError:
        print("Coin Catcher icon not found.")

# Fungsi untuk memulai game
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

# Fungsi untuk menunggu dan mengklik tombol "Back to Games"
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

# Fungsi untuk mencari dan klik berdasarkan warna RGB
def click_on_RGBpixel(r_value, g_value, b_value, coords):
    pic = pyautogui.screenshot(region=coords)
    for x in range(0, coords[2], 6):
        for y in range(0, coords[3], 6):
            r, g, b = pic.getpixel((x, y))
            if r == r_value and g == g_value and b == b_value:
                pyautogui.click(x + coords[0], y + coords[1])
                return True
    return False

# Fungsi untuk mengikuti arah bola dan mengkliknya
def follow_ball(r_value, g_value, b_value):
    scan_region = (0, 0, screen_width, screen_height)  # Mengambil screenshot seluruh layar
    print("Starting ball tracking...")
    
    while True:
        ball_detected = click_on_RGBpixel(r_value, g_value, b_value, scan_region)
        if ball_detected:
            print("Ball detected and clicked!")
        else:
            print("Ball not detected, retrying...")
        time.sleep(0.01)  # Tambahkan sedikit delay agar tidak terlalu sering refresh

# Fungsi utama permainan
def play():
    print("Starting play function...")
    follow_ball(BALL_COLOR[0], BALL_COLOR[1], BALL_COLOR[2])

# Fungsi untuk mengecek kemenangan
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
    select_coincatcher()
    time.sleep(4)
    start()
    time.sleep(5)
    play()  # Will run and track the ball
    time.sleep(7)
    backtogames()

def main():
    chrome_open()
    time.sleep(1)
    select_coincatcher()
    time.sleep(4)
    start()
    time.sleep(5)
    play()  # Will run and track the ball
    time.sleep(7)
    backtogames()