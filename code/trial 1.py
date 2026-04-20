from ble_keyboard import BLEKeyboard
from machine import Pin, TouchPad
import time

# 1. Initialize the Bluetooth Keyboard
kb = BLEKeyboard("FBWGMat")

# 2. Initialize Touch Pins
fireboy_left  = TouchPad(Pin(15))
fireboy_right = TouchPad(Pin(13))
fireboy_jump  = TouchPad(Pin(12))

watergirl_left  = TouchPad(Pin(14))
watergirl_right = TouchPad(Pin(27))
watergirl_jump  = TouchPad(Pin(33))

# 3. Set the Touch Threshold
THRESHOLD = 500

print("Waiting for Bluetooth connection...")
connection_ready = False

while True:
    if kb.is_connected():
        if not connection_ready:
            print("Connected! Waiting 2 seconds for OS security handshake...")
            time.sleep(2)
            print("Ready! Step on the mat.")
            connection_ready = True

        try:
            val_fb_l = fireboy_left.read()
            val_fb_r = fireboy_right.read()
            val_fb_j = fireboy_jump.read()
            val_wg_l = watergirl_left.read()
            val_wg_r = watergirl_right.read()
            val_wg_j = watergirl_jump.read()

            # --- Fireboy: Arrow keys ---
            if val_fb_l < THRESHOLD:
                print(f"Fireboy LEFT (val: {val_fb_l})")
                kb.arrow_left()
                while fireboy_left.read() < THRESHOLD:
                    time.sleep_ms(20)
                time.sleep_ms(100)

            elif val_fb_r < THRESHOLD:
                print(f"Fireboy RIGHT (val: {val_fb_r})")
                kb.arrow_right()
                while fireboy_right.read() < THRESHOLD:
                    time.sleep_ms(20)
                time.sleep_ms(100)

            elif val_fb_j < THRESHOLD:
                print(f"Fireboy JUMP (val: {val_fb_j})")
                kb.arrow_up()
                while fireboy_jump.read() < THRESHOLD:
                    time.sleep_ms(20)
                time.sleep_ms(100)

            # --- Watergirl: WASD ---
            elif val_wg_l < THRESHOLD:
                print(f"Watergirl LEFT (val: {val_wg_l})")
                kb.type_text("a")
                while watergirl_left.read() < THRESHOLD:
                    time.sleep_ms(20)
                time.sleep_ms(100)

            elif val_wg_r < THRESHOLD:
                print(f"Watergirl RIGHT (val: {val_wg_r})")
                kb.type_text("d")
                while watergirl_right.read() < THRESHOLD:
                    time.sleep_ms(20)
                time.sleep_ms(100)

            elif val_wg_j < THRESHOLD:
                print(f"Watergirl JUMP (val: {val_wg_j})")
                kb.type_text("w")
                while watergirl_jump.read() < THRESHOLD:
                    time.sleep_ms(20)
                time.sleep_ms(100)

        except ValueError:
            pass

    else:
        connection_ready = False

    time.sleep_ms(50)