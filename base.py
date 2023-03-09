import pywinio
import time
import atexit

# KeyBoard Commands
# Command port
KBC_KEY_CMD = 0x64
# Data port
KBC_KEY_DATA = 0x60

g_winio = None


def get_winio():
    global g_winio

    if g_winio is None:
        g_winio = pywinio.WinIO()

        def __clear_winio():
            global g_winio
            g_winio = None
        atexit.register(__clear_winio)

    return g_winio


def wait_for_buffer_empty():
    '''
    Wait keyboard buffer empty
    '''

    winio = get_winio()

    dwRegVal = 0x02
    while (dwRegVal & 0x02):
        dwRegVal = winio.get_port_byte(KBC_KEY_CMD)


def key_down(scancode):
    winio = get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode)


def key_up(scancode):
    winio = get_winio()

    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_CMD, 0xd2)
    wait_for_buffer_empty()
    winio.set_port_byte(KBC_KEY_DATA, scancode | 0x80)


def key_press(scancode, press_time=0.2):
    key_down(scancode)
    time.sleep(press_time)
    key_up(scancode)


# Press 'A' key
# Scancodes references : https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html
key_q = 0x10
key_w = 0x11
key_e = 0x12
key_r = 0x13
key_t = 0x14
key_y = 0x15

key_1 = 0x02
key_2 = 0x03
key_3 = 0x04
key_4 = 0x05
key_5 = 0x06


key_UpArrow = 0x48
key_DownArrow = 0x50
key_Left = 0x4b
key_Right = 0x4d

key_LAlt = 0x38
key_LCtrl = 0x1d
key_LShift = 0x2a
key_space = 0x39

key_del = 0x53
key_ins = 0x52
key_PGDN = 0x51
key_PGUP = 0x49
key_end = 0x4f 

key_F8 = 0x42
key_F10 = 0x44 
