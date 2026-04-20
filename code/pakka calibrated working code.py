from machine import Pin, time_pulse_us
import time
import struct

# ==============================
# BLE KEYBOARD INIT
# ==============================
kb = BLEKeyboard("FBWGMat")

# ==============================
# FIREBOY SENSORS (Arrow Keys)
# ==============================
trig_j = Pin(22, Pin.OUT)
echo_j = Pin(23, Pin.IN)

trig_r = Pin(19, Pin.OUT)
echo_r = Pin(21, Pin.IN)

trig_l = Pin(5, Pin.OUT)
echo_l = Pin(18, Pin.IN)

# ==============================
# WATERGIRL SENSORS (W A D)
# ==============================
trig_wj = Pin(13, Pin.OUT)
echo_wj = Pin(12, Pin.IN)

trig_wr = Pin(14, Pin.OUT)
echo_wr = Pin(27, Pin.IN)

trig_wl = Pin(26, Pin.OUT)
echo_wl = Pin(25, Pin.IN)

# ==============================
# SETTINGS
# ==============================

# 🔥 Fireboy (BALANCED)
FB_MIN_CM = 2.0
FB_MAX_CM = 5.0

# 💧 Watergirl (UNCHANGED)
WG_MIN_CM = 1.5
WG_MAX_CM = 4.0

# HID KEYCODES
KEY_LEFT  = 0x50
KEY_RIGHT = 0x4F
KEY_UP    = 0x52

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
# SMOOTHED DISTANCE
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
def is_triggered(dist, min_cm, max_cm):
    return min_cm < dist < max_cm and dist < 8  # extra safety cap

# ==============================
# MAIN LOOP
# ==============================
print("Waiting for Bluetooth connection...")
connection_ready = False

while True:
    if kb.is_connected():

        if not connection_ready:
            print("Connected! Stabilizing...")
            time.sleep(2)
            print("Ready!")
            connection_ready = True

        try:
            # -------- FIREBOY --------
            j_cm = get_avg_distance(trig_j, echo_j)
            r_cm = get_avg_distance(trig_r, echo_r)
            l_cm = get_avg_distance(trig_l, echo_l)

            # -------- WATERGIRL --------
            wj_cm = get_avg_distance(trig_wj, echo_wj)
            wr_cm = get_avg_distance(trig_wr, echo_wr)
            wl_cm = get_avg_distance(trig_wl, echo_wl)

            # -------- CONDITIONS --------
            # Fireboy (balanced)
            jump_active  = is_triggered(j_cm, FB_MIN_CM, FB_MAX_CM)
            right_active = is_triggered(r_cm, FB_MIN_CM, FB_MAX_CM)
            left_active  = is_triggered(l_cm, FB_MIN_CM, FB_MAX_CM)

            # Watergirl (unchanged)
            wj_active = is_triggered(wj_cm, WG_MIN_CM, WG_MAX_CM)
            wr_active = is_triggered(wr_cm, WG_MIN_CM, WG_MAX_CM)
            wl_active = is_triggered(wl_cm, WG_MIN_CM, WG_MAX_CM)

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

            # HID limit
            active_keys = active_keys[:6]

            # pad to 6 keys
            active_keys += [0] * (6 - len(active_keys))

            # send keys
            kb._send(struct.pack("8B", 0, 0, *active_keys))

        except Exception as e:
            print("Error:", e)

    else:
        kb._send(b"\x00" * 8)
        connection_ready = False

    time.sleep_ms(20)