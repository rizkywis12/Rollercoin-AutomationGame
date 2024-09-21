import random
import time
from loguru import logger
# from helicopter import main as helicopter_main
from coinc import main as coinc_main
from cryptonoid import main as cryptonoid_main
from coinfisher import main as coinfisher_main
from game2048 import main as game2048_main

# Konfigurasi logger
logger.add("game_log.log", format="{time} {level} {message}", level="INFO", rotation="10 MB")

# List dari game yang tersedia
games = [coinc_main, cryptonoid_main, coinfisher_main, game2048_main]
game_names = ["Helicopter", "Coinc", "Cryptonoid", "Coin Fisher", "2048"]

# Fungsi untuk memilih game awal
def select_game():
    logger.info("Memulai proses pemilihan game.")
    print("Pilih game yang ingin dimainkan:")
    # print("1. Helicopter")
    print("2. Coinc")
    print("3. Cryptonoid")
    print("4. Coin Fisher")
    print("5. 2048")
    
    try:
        choice = int(input("Masukkan nomor game: "))
        if 1 <= choice <= 5:
            logger.info(f"Game {game_names[choice - 1]} telah dipilih oleh pengguna.")
            return games[choice - 1], game_names[choice - 1]
        else:
            logger.warning("Pilihan tidak valid. Pengguna memasukkan angka di luar rentang 1-5.")
            return select_game()
    except ValueError:
        logger.error("Pengguna memasukkan input yang tidak valid (bukan angka).")
        return select_game()

# Jalankan game yang dipilih secara manual terlebih dahulu
game, game_name = select_game()
logger.info(f"Memulai game {game_name}.")
game()

# Setelah game pertama selesai, jalankan game lain secara acak
while True:
    logger.info(f"Game {game_name} selesai dijalankan. Menunggu 5 detik sebelum game berikutnya.")
    time.sleep(5)
    
    # Pilih game secara acak dari daftar
    game, game_name = random.choice(list(zip(games, game_names)))
    
    logger.info(f"Game {game_name} dipilih secara acak untuk dimainkan.")
    game()
    
    time.sleep(1)  # Tunggu 1 detik sebelum memulai game baru

# Memberi info script telah selesai
logger.info("Semua game telah selesai. Script selesai dijalankan.")
