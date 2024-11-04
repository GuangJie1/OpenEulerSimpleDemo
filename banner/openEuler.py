import pyfiglet
import time
import os

text = "Hello, openEuler!"
ascii_banner = pyfiglet.figlet_format(text)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

for i in range(1, len(ascii_banner) + 1):
    clear_screen()
    print(ascii_banner[:i])
    time.sleep(0.05)
