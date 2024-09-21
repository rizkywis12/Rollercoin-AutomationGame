import pyautogui
import pyscreeze
import time

# Disable exceptions for image not found
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

# Dapatkan ukuran layar penuh secara otomatis
screen_width, screen_height = pyautogui.size()

# Warna bola yang akan diikuti (RGB)
BALL_COLOR = (162, 192, 197)

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

def select_coincatcher():
    """Pilih game Coin Catcher, jika tidak ditemukan setelah 5 kali percobaan, kembali ke halaman utama dan hentikan bot."""
    print("Searching for Coin Catcher...")
    location = retry_find_image("img/cryptonoid.png", retries=5, confidence=0.9)
    if location:
        pyautogui.click(location[0], location[1] + 33)
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
def follow_ball(r_value, g_value, b_value, max_time=60):
    scan_region = (0, 0, screen_width, screen_height)  # Mengambil screenshot seluruh layar
    print("Starting ball tracking...")
    start_time = time.time()  # Waktu mulai pelacakan bola
    
    while time.time() - start_time < max_time:
        ball_detected = click_on_RGBpixel(r_value, g_value, b_value, scan_region)
        if ball_detected:
            print("Ball detected and clicked!")
        else:
            print("Ball not detected, retrying...")
        
        time.sleep(0.001)  # Tambahkan sedikit delay agar tidak terlalu sering refresh

    print("Ball tracking ended after 60 seconds.")

# Fungsi utama permainan
def play():
    print("Starting play function...")
    last_check_time = time.time()  # Waktu terakhir pengecekan kemenangan/kekalahan

    # Jalankan pelacakan bola selama 60 detik
    follow_ball(BALL_COLOR[0], BALL_COLOR[1], BALL_COLOR[2], max_time=60)

    # Setelah pelacakan selesai, periksa hasil
    return victory_or_defeat_check()  # Memeriksa hasil setelah pelacakan berhenti

# Fungsi untuk mengecek kemenangan atau kekalahan
def victory_or_defeat_check():
    print("Checking for victory or defeat...")

    # Cek untuk victory
    victory_location = pyautogui.locateCenterOnScreen("img/victory.png", confidence=0.9)
    if victory_location:
        print("Victory detected! Clicking 'Victory'.")
        pyautogui.click(victory_location)
        return "victory"

    # Cek untuk defeat
    defeat_location = pyautogui.locateCenterOnScreen("img/defeat.png", confidence=0.9)
    if defeat_location:
        print("Defeat detected! Clicking 'Defeat'.")
        pyautogui.click(defeat_location)
        return "defeat"

    return None  # Tidak ada kondisi kemenangan atau kekalahan yang terdeteksi

if __name__ == "__main__":
    chrome_open()
    time.sleep(1)
    if select_coincatcher():  # Hanya lanjutkan jika select_coincatcher berhasil
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


def main():
    chrome_open()
    time.sleep(1)
    select_coincather()
    time.sleep(4)
    start()
    time.sleep(5)
    play()  # Will run and track the ball
    time.sleep(7)
    backtogames()