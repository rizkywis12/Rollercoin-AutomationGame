import pyautogui
import time

print("Tekan Ctrl+C untuk berhenti")

try:
    while True:
        # Dapatkan posisi mouse
        x, y = pyautogui.position()
        print(f"Koordinat: X={x} Y={y}", end="\r")  # end="\r" agar hasilnya selalu di-overwrite pada baris yang sama
        time.sleep(0.1)  # Untuk memperlambat update, bisa disesuaikan
except KeyboardInterrupt:
    print("\nProses dihentikan.")
