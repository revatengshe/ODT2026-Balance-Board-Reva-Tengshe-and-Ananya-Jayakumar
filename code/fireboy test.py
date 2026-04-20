from ble_keyboard import BLEKeyboard
from machine import Pin, time_pulse_us
import time
import struct

# ==============================
# BLE KEYBOARD INIT
# ==============================
kb = BLEKeyboard("Fireboy_Test")

# ==============================
# FIREBOY SENSORS
# ==============================
trig_j = Pin(22, Pin.OUT)  # Jump (↑)
echo_j = Pin(23, Pin.IN)

trig_r = Pin(19, Pin.OUT)  # Right (→)
echo_r = Pin(21, Pin.IN)

trig_l = Pin(5, Pin.OUT)   # Left (←)
echo_l = Pin(18, Pin.IN)

# ==============================
# TILT SETTINGS
# ==============================
MIN_CM = 1.5
MAX_CM = 4.0

# HID KEYCODES
KEY_LEFT  = 0x50
KEY_RIGHT = 0x4F
KEY_UP    = 0x52

# ==============================
# DISTANCE FUNCTION
# ==============================
def get_distance(trig, echo):
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    duration = time_pulse_us(echo, 1, 30000)

    if duration < 0:
        return 999

    return (duration / 2) / 29.1

# ==============================
# SMOOTHING
# ==============================
def get_avg_distance(trig, echo):
    vals = []
    for _ in range(3):
        vals.append(get_distance(trig, echo))
        time.sleep_ms(5)
    return sum(vals) / len(vals)

# ==============================
# TRIGGER CHECK
# ==============================
def is_triggered(dist):
    return MIN_CM < dist < MAX_CM

# ==============================
# MAIN LOOP
# ==============================
print("Waiting for Bluetooth connection...")
connected = False

while True:
    if kb.is_connected():

        if not connected:
            print("Connected! Ready for Fireboy controls")
            time.sleep(2)
            connected = True

        try:
            # Read distances
            j_cm = get_avg_distance(trig_j, echo_j)
            r_cm = get_avg_distance(trig_r, echo_r)
            l_cm = get_avg_distance(trig_l, echo_l)

            # Check triggers
            jump_active  = is_triggered(j_cm)
            right_active = is_triggered(r_cm)
            left_active  = is_triggered(l_cm)

            print(f"J={j_cm:.1f} R={r_cm:.1f} L={l_cm:.1f}")

            # Build key list
            active_keys = []

            if jump_active:  active_keys.append(KEY_UP)
            if right_active: active_keys.append(KEY_RIGHT)
            if left_active:  active_keys.append(KEY_LEFT)

            # Limit to 6 keys
            active_keys = active_keys[:6]
            active_keys += [0] * (6 - len(active_keys))

            # Send keys
            kb._send(struct.pack("8B", 0, 0, *active_keys))

        except Exception as e:
            print("Error:", e)

    else:
        kb._send(b"\x00" * 8)
        connected = False

    time.sleep_ms(20)