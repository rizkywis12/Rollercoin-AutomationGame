import pyautogui
import time
from pynput.mouse import Listener
from PIL import ImageGrab

# Variabel global untuk menyimpan koordinat mouse
start_pos = None
end_pos = None

def on_click(x, y, button, pressed):
    global start_pos, end_pos
    if pressed:
        # Simpan posisi awal ketika mouse di-klik
        start_pos = (x, y)
        print(f"Start position: {start_pos}")
    else:
        # Simpan posisi akhir ketika mouse dilepas
        end_pos = (x, y)
        print(f"End position: {end_pos}")
        
        # Hitung lebar dan tinggi dari area yang di-drag
        width = abs(end_pos[0] - start_pos[0])
        height = abs(end_pos[1] - start_pos[1])
        print(f"Width: {width}, Height: {height}")
        
        # Ambil tangkapan layar dari area yang di-drag
        capture_screenshot(start_pos, end_pos)

        # Stop listener setelah drag selesai
        return False

def capture_screenshot(start_pos, end_pos):
    # Urutkan koordinat agar sesuai dengan area yang benar
    left = min(start_pos[0], end_pos[0])
    top = min(start_pos[1], end_pos[1])
    right = max(start_pos[0], end_pos[0])
    bottom = max(start_pos[1], end_pos[1])
    
    # Ambil screenshot dari area yang di-drag
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot.show()  # Tampilkan hasil tangkapan layar
    screenshot.save("snipped_area.png")  # Simpan tangkapan layar

def start_snipping():
    print("Drag mouse to select an area...")
    with Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    time.sleep(2)  # Tunggu 2 detik sebelum memulai agar kamu siap
    start_snipping()
