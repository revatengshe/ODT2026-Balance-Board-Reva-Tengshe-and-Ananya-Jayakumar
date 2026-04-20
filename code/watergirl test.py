from ble_keyboard import BLEKeyboard
from machine import Pin, time_pulse_us
import time
import struct

# ==============================
# BLE KEYBOARD INIT
# ==============================
kb = BLEKeyboard("Watergirl_Test")

# ==============================
# WATERGIRL SENSORS
# ==============================
trig_wj = Pin(13, Pin.OUT)  # Jump (W)
echo_wj = Pin(12, Pin.IN)

trig_wr = Pin(14, Pin.OUT)  # Right (D)
echo_wr = Pin(27, Pin.IN)

trig_wl = Pin(26, Pin.OUT)  # Left (A)
echo_wl = Pin(25, Pin.IN)

# ==============================
# TILT SETTINGS
# ==============================
MIN_CM = 1.5
MAX_CM = 4.0

# HID KEYCODES
KEY_W = 0x1A
KEY_A = 0x04
KEY_D = 0x07

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
            print("Connected! Ready for Watergirl controls")
            time.sleep(2)
            connected = True

        try:
            # Read distances
            wj_cm = get_avg_distance(trig_wj, echo_wj)
            wr_cm = get_avg_distance(trig_wr, echo_wr)
            wl_cm = get_avg_distance(trig_wl, echo_wl)

            # Check triggers
            jump_active  = is_triggered(wj_cm)
            right_active = is_triggered(wr_cm)
            left_active  = is_triggered(wl_cm)

            print(f"W={wj_cm:.1f} D={wr_cm:.1f} A={wl_cm:.1f}")

            # Build key list
            active_keys = []

            if jump_active:  active_keys.append(KEY_W)
            if right_active: active_keys.append(KEY_D)
            if left_active:  active_keys.append(KEY_A)

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