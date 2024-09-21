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


# def select_coincather():
#     try:
#         x, y = pyautogui.locateCenterOnScreen("img/coinfisher.png", confidence=0.8)
#         pyautogui.click(x, y + 40)
#     except TypeError:
#         print("Coin Catcher icon not found.")
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
    """Pilih game Coin Catcher, jika tidak ditemukan setelah 5 kali percobaan, kembali ke halaman utama dan hentikan bot."""
    print("Searching for Coin Catcher...")
    location = retry_find_image("img/coinfisher.png", retries=5, confidence=0.8)
    if location:
        pyautogui.click(location[0], location[1] + 40)
        print("Coin Catcher selected.")
    else:
        print("Coin Catcher not found after 5 attempts. Returning to home and stopping bot.")
        backhome()
        return False  # Hentikan bot
    return True  # Lanjutkan jika ditemukan

def start():
    print("Searching for the 'Start' button...")
    location = retry_find_image("img/start2.png")
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
        # Cek kemenangan atau kekalahan setiap detik
        result = victory_or_defeat_check()
        if result == "victory":
            print("Victory detected! Exiting play function.")
            return "victory"  # Mengembalikan status kemenangan
        elif result == "defeat":
            print("Defeat detected! Exiting play function.")
            return "defeat"  # Mengembalikan status kekalahan
        
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

def victory_or_defeat_check():
    """Memeriksa apakah kondisi kemenangan atau kekalahan tercapai."""
    print("Checking for victory or defeat...")

    # Cek untuk victory
    victory_location = pyautogui.locateCenterOnScreen("img/victory.png", confidence=0.9)
    if victory_location:
        print("Victory detected! Clicking 'Victory'.")
        pyautogui.click(victory_location)  # Klik gambar kemenangan
        return "victory"

    # Cek untuk defeat
    defeat_location = pyautogui.locateCenterOnScreen("img/defeat.png", confidence=0.9)
    if defeat_location:
        print("Defeat detected! Clicking 'Defeat'.")
        pyautogui.click(defeat_location)  # Klik gambar kekalahan
        return "defeat"

    return None  # Tidak ada kondisi kemenangan atau kekalahan yang terdeteksi


if __name__ == "__main__":
    chrome_open()
    time.sleep(1)
    if select_coincather():  # Hanya lanjutkan jika select_coincather berhasil
        time.sleep(4)
        start()
        time.sleep(5)
        
        # Dapatkan hasil dari play()
        result = play()  # Akan mengembalikan "victory" atau "defeat"
        
        if result == "victory":
            time.sleep(7)
            gain()  # Hanya panggil gain jika menang
            backtogames()
        elif result == "defeat":
            print("Game over. Bot stopped after defeat.")
            # Tidak perlu lanjut ke gain, langsung keluar

def main():
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