import subprocess
import serial
import keyboard
import os
import sys
import time
import webbrowser
from datetime import datetime

# Replace with the correct COM port and baud rate
COM_PORT = "COM4"  # On Linux/Mac, use '/dev/ttyUSB0'
BAUD_RATE = 115200

# Dictionary to store app names and their paths
APP_PATHS = {
    "CALCULATOR": "calc.exe",
    "DISCORD": r"C:\\Users\\bhuva\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk",
    "WHATSAPP": r"C:\\Users\\YourUsername\\AppData\\Local\\WhatsApp\\WhatsApp.exe",
    "PHOTOSHOP": r"I:\\Adobe\\Photoshop_2021\\Adobe Photoshop 2021\\Photoshop.exe",
    "OBS": r"C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe",
    "VSCODE": r"C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "PUTTY": r"C:\\Program Files\\PuTTY\\putty.exe",
    "NOTION": r"C:\\Users\\bhuva\\AppData\\Local\\Programs\\Notion\\Notion.exe",

}

# Dictionary for common actions (micros)
MICROS = {
    "CUT": lambda: keyboard.press_and_release("ctrl+x"),
    "COPY": lambda: keyboard.press_and_release("ctrl+c"),
    "PASTE": lambda: keyboard.press_and_release("ctrl+v"),
    "TEXT_EXTRACTOR": lambda: keyboard.press_and_release("win+shift+t"),
    "HOME": lambda: keyboard.press_and_release("win+d"),
    "SLEEP": lambda: os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") if sys.platform == "win32" else print("Sleep not supported on this OS."),
    "OPEN_URL": lambda url: os.system(f"start {url}"),
    "TYPE_TEXT": lambda text: keyboard.write(text),
    "OPEN_APP": lambda app_name: os.system(f'start "" "{APP_PATHS.get(app_name, "")}"') if app_name in APP_PATHS else print(f"App not found: {app_name}"),
    "NETFLIX": lambda: subprocess.run(["explorer.exe", "shell:AppsFolder\\4DF9E0F8.Netflix_mcm4njqhnhss8!Netflix.App"],check=True),
    "SPOTIFY": lambda: subprocess.run(["explorer.exe", "shell:AppsFolder\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify"],check=True),
    "YOUTUBE": lambda: webbrowser.open("https://www.youtube.com"),
    "AMAZON": lambda: webbrowser.open("https://www.amazon.in"),
    "GITHUB": lambda: webbrowser.open("https://www.youtube.com"),
    "INSTAGRAM": lambda: subprocess.run(["explorer.exe", "shell:AppsFolder\\Facebook.InstagramBeta_8xx8rvfyw5nnt!App"],check=True),
}

# Dictionary for macro actions
MACROS = {
    "YOUTUBE_VIDEO": [
        ("OPEN_URL", "https://youtube.com/watch?v=xyz"),
    ],
    "WRITE_NOTE": [
        ("OPEN_APP", "notepad"),
        ("TYPE_TEXT", "Hello, this is a note!"),
        ("KEY_PRESS", "ctrl+s"),
    ],
}

def perform_action(data):
    """
    Executes a single action based on the received data.
    """
    try:
        print(f"Performing action: {data}")

        # Split command and argument (e.g., "OPEN_URL,https://example.com")
        if "," in data:
            command, argument = data.split(",", 1)
            command, argument = command.strip(), argument.strip()
        else:
            command, argument = data.strip(), None

        # Execute micros (single actions)
        if command in MICROS:
            if argument:
                MICROS[command](argument)
            else:
                MICROS[command]()
        # Execute macros (sequence of actions)
        elif command in MACROS:
            perform_macro(command)
        else:
            print(f"Unknown command: {command}")
    except Exception as e:
        print(f"Error in perform_action: {e}")

def perform_macro(macro_name):
    """
    Executes a sequence of actions defined in the MACROS dictionary.
    """
    if macro_name in MACROS:
        for action, argument in MACROS[macro_name]:
            if action in MICROS:
                if argument:
                    MICROS[action](argument)
                else:
                    MICROS[action]()
            else:
                print(f"Unknown action in macro: {action}")
    else:
        print(f"Unknown macro: {macro_name}")

def main():
    """
    Main function to handle serial communication and execute commands.
    """
    print("Connecting to ESP32-S3...")
    try:
        with serial.Serial(COM_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Connected to {COM_PORT}")
            while True:
                if ser.in_waiting > 0:
                    data = ser.readline().decode("utf-8").strip()
                    print(f"Received: {data}")
                    perform_action(data)
    except serial.SerialException as e:
        print(f"Serial Communication Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully...")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
