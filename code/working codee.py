from ble_keyboard import BLEKeyboard
from machine import Pin, TouchPad
import struct
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

THRESHOLD = 350

# HID keycodes
KEY_LEFT  = 0x50
KEY_RIGHT = 0x4F
KEY_UP    = 0x52
KEY_A     = 0x04
KEY_D     = 0x07
KEY_W     = 0x1A

# Track what's currently held down
held = {
    'fb_l': False, 'fb_r': False, 'fb_j': False,
    'wg_l': False, 'wg_r': False, 'wg_j': False,
}

def press(keycode, modifier=0):
    kb._send(struct.pack("8B", modifier, 0, keycode, 0, 0, 0, 0, 0))

def release():
    kb._send(b"\x00" * 8)

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
            touches = {
                'fb_l': fireboy_left.read()    < THRESHOLD,
                'fb_r': fireboy_right.read()   < THRESHOLD,
                'fb_j': fireboy_jump.read()    < THRESHOLD,
                'wg_l': watergirl_left.read()  < THRESHOLD,
                'wg_r': watergirl_right.read() < THRESHOLD,
                'wg_j': watergirl_jump.read()  < THRESHOLD,
            }

            keys = {
                'fb_l': KEY_LEFT,  'fb_r': KEY_RIGHT, 'fb_j': KEY_UP,
                'wg_l': KEY_A,     'wg_r': KEY_D,     'wg_j': KEY_W,
            }

            for pad, touched in touches.items():
                if touched and not held[pad]:
                    print(f"{pad} held down")
                    held[pad] = True
                elif not touched and held[pad]:
                    print(f"{pad} released")
                    held[pad] = False

            # Collect ALL active keys across both players into 6 slots
            active_keys = [keys[pad] for pad, touched in touches.items() if touched]
            active_keys += [0] * (6 - len(active_keys))
            kb._send(struct.pack("8B", 0, 0, *active_keys))

        except ValueError:
            pass

    else:
        held = {k: False for k in held}
        connection_ready = False

    time.sleep_ms(20)