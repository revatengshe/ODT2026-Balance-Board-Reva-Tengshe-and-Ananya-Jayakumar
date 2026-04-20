from ble_keyboard import BLEKeyboard
from machine import Pin, time_pulse_us
import time
import struct

# =============================
# dBLE KEYBOARD INIT
# ==============================
kb = BLEKeyboard("FBWGMat")

# ==============================
# FIREBOY SENSORS (Arrow Keys)
# ==============================
dtrig_j = Pin(22, Pin.OUT)  # Jump
echo_j = Pin(23, Pin.IN)
d
trig_r = Pin(19, Pin.OUT)  # Right
echo_r = Pin(21, Pin.IN)

trig_l = Pin(5, Pin.OUT)   # Leftd
echo_l = Pin(18, Pin.IN)

# ==============================
# WATERGIRL SENSORS (W A D)
# ==============================
trig_wj = Pin(13, Pin.OUT)  # Jump (W)
echo_wj = Pin(12, Pin.IN)

trig_wr = Pin(14, Pin.OUT)  # Right (D)
echo_wr = Pin(27, Pin.IN)

trig_wl = Pin(26, Pin.OUT)  # Left (A)
echo_wl = Pin(25, Pin.IN)

# ==============================
# SETTINGS
# ==============================
TRIGGER_CM = 15

# HID KEYCODES
KEY_LEFT  = 0x50
KEY_RIGHT = 0x4F
KEY_UP    = 0x52

KEY_W = 0x1A
KEY_A = 0x04
KEY_D = 0x07

# ==============================
# FUNCTION: DISTANCE
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
# MAIN LOOP
# ==============================
print("Waiting for Bluetooth connection...")
connection_ready = False

while True:
    if kb.is_connected():
        if not connection_ready:
            print("Connected! Waiting 2 seconds for OS handshake...")
            time.sleep(2)
            print("Ready!")
            connection_ready = True

        try:
            # -------- FIREBOY --------
            j_cm = get_distance(trig_j, echo_j)
            time.sleep_ms(15)
            r_cm = get_distance(trig_r, echo_r)
            time.sleep_ms(15)
            l_cm = get_distance(trig_l, echo_l)
            time.sleep_ms(15)

            # -------- WATERGIRL --------
            wj_cm = get_distance(trig_wj, echo_wj)
            time.sleep_ms(15)
            wr_cm = get_distance(trig_wr, echo_wr)
            time.sleep_ms(15)
            wl_cm = get_distance(trig_wl, echo_wl)
            time.sleep_ms(15)

            # -------- CONDITIONS --------
            jump_active  = j_cm < TRIGGER_CM
            right_active = r_cm < TRIGGER_CM
            left_active  = l_cm < TRIGGER_CM

            wj_active = wj_cm < TRIGGER_CM
            wr_active = wr_cm < TRIGGER_CM
            wl_active = wl_cm < TRIGGER_CM

            print(
                f"FB: J={j_cm:.1f} R={r_cm:.1f} L={l_cm:.1f} | "
                f"WG: J={wj_cm:.1f} R={wr_cm:.1f} L={wl_cm:.1f}"
            )

            # -------- KEY BUILD --------
            active_keys = []

            # Fireboy
            if jump_active:  active_keys.append(KEY_UP)
            if right_active: active_keys.append(KEY_RIGHT)
            if left_active:  active_keys.append(KEY_LEFT)

            # Watergirl
            if wj_active: active_keys.append(KEY_W)
            if wr_active: active_keys.append(KEY_D)
            if wl_active: active_keys.append(KEY_A)

            # Limit to 6 keys (HID limit)
            active_keys = active_keys[:6]

            # Pad remaining slots
            active_keys += [0] * (6 - len(active_keys))

            # Send keys
            kb._send(struct.pack("8B", 0, 0, *active_keys))

        except Exception as e:
            print("Error:", e)

    else:
        # release all keys when disconnected
        kb._send(b"\x00" * 8)
        connection_ready = False

    time.sleep_ms(20)
