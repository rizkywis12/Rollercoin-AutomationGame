import pyautogui
from PIL import ImageGrab
from pynput import mouse

def get_color_at_mouse(x, y):
    # Ambil screenshot di area kecil di sekitar posisi mouse
    screen = ImageGrab.grab(bbox=(x, y, x+1, y+1))

    # Ambil warna pixel pada posisi mouse
    color = screen.getpixel((0, 0))
    return color

def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        color = get_color_at_mouse(x, y)
        print(f"Posisi: ({x}, {y}), Kode warna RGB: {color}")

def main():
    print("Klik kanan pada area yang ingin diambil warnanya. Tekan Ctrl+C untuk keluar.")
    # Set up listener untuk klik mouse
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()
