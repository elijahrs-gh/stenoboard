import board
import neopixel
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.steno import Steno

keyboard = KMKKeyboard()
keyboard.extensions.append(Steno())

keyboard.col_pins = (
    board.GP0,  # Col 0
    board.GP1,  # Col 1
    board.GP2,  # Col 2
    board.GP3,  # Col 3
    board.GP4,  # Col 4
    board.GP5,  # Col 5
    board.GP7,  # Col 6
    board.GP8,  # Col 7
)

keyboard.row_pins = (
    board.GP10,  # Row 0
    board.GP11,  # Row 1
    board.GP12,  # Row 2
    board.GP13,  # Row 3
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

pixels = neopixel.NeoPixel(board.GP6, 2, brightness=0.2, auto_write=False)
pixels.fill((0, 8, 0))
pixels.show()

def after_scan(task):
    r, g, b = pixels[0]
    pixels[0] = (r ^ 1, g, b)
    pixels.show()

keyboard.after_hid_send.append(after_scan)

keyboard.keymap = [
    [
        KC.STN_S1, KC.STN_TL, KC.STN_PL, KC.STN_HL, KC.STN_ST1, KC.STN_FR, KC.STN_PR, KC.STN_LR,
        KC.STN_S2, KC.STN_KL, KC.STN_WL, KC.STN_RL, KC.STN_ST2, KC.STN_RR, KC.STN_BR, KC.STN_GR,
        KC.STN_N1, KC.STN_A,  KC.STN_O,  KC.NO,     KC.NO,      KC.STN_E,  KC.STN_U, KC.STN_N2,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()

