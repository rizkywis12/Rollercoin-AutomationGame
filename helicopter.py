import pyautogui
import pyscreeze
import time
import cv2
import numpy as np

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
        x, y = pyautogui.locateCenterOnScreen("img/flappyrocket.png", confidence=0.8)
        pyautogui.click(x, y + 40)
    except TypeError:
        print("Coin Catcher icon not found.")
        
def collect_reward():
    print("Searching for 'Collect Reward' image...")
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen("img/collectreward.png", confidence=0.9)
            pyautogui.click(x, y)
            print("Clicked 'Collect Reward'.")
            break  # Exit the loop after clicking
        except TypeError:
            print("'Collect Reward' image not found. Retrying...")
            time.sleep(1)  # Wait for 1 second before checking again

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

def play():
    print("Starting play function...")

    # Tambahkan beberapa klik awal untuk menjaga helikopter tetap mengudara
    for _ in range(1): 
        pyautogui.click()
        time.sleep(0.05)

    start_time = time.time()  # Catat waktu mulai
    while time.time() - start_time < 50:  # Bermain hingga 50 detik
         # Check for victory every second
        if victory_check():
            print("Victory detected! Exiting play function.")
            break
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Deteksi warna helikopter (dengan sedikit toleransi warna)
        lower_color = np.array([60, 160, 240])  # Batas bawah warna (BGR)
        upper_color = np.array([90, 190, 270])  # Batas atas warna (BGR)
        mask = cv2.inRange(frame, lower_color, upper_color)

        # Temukan kontur helikopter
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)

            helicopter_center_x = x + w // 2
            helicopter_center_y = y + h // 2

            screen_center_y = screen_height // 2
            distance_from_center = abs(helicopter_center_y - screen_center_y)

            # Penyesuaian frekuensi klik berdasarkan jarak dari tengah
            if distance_from_center > 80:
                pyautogui.click()  # Klik lebih sering jika jauh dari tengah
                time.sleep(0.05) 
            elif distance_from_center > 50:
                pyautogui.click()
                time.sleep(0.07)

        time.sleep(0.06) 

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
    time.sleep(1) # Berikan sedikit waktu setelah menekan tombol start
    play() 
    time.sleep(7)
    gain()
    collect_reward()  # Add this line to collect the reward
    backtogames()

def main():
    chrome_open()
    time.sleep(1)
    select_coincather()
    time.sleep(6)
    start()
    time.sleep(1) # Berikan sedikit waktu setelah menekan tombol start
    play() 
    time.sleep(7)
    gain()
    collect_reward()  # Add this line to collect the reward
    backtogames()