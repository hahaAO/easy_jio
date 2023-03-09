import base
import time

# 计算机从键盘上扫走一次key_down或key_up需要的时间
scan_time = 0.0044


class key_event:
    key_code: int
    wait = True
    press_time: int


class up_event:
    key_code: int
    delay_time: int


game_time = 0.0

event_list = []


def total_time():
    global game_time
    for event in event_list:
        game_time += 2*scan_time
        if (event.wait):
            game_time += event.press_time
    return game_time


def execute():
    up_event_list = []
    for event in event_list:
        if (event.wait):
            up_event_list.remove() 
            # TODO execute up_event
            base.key_down(event.key_code)
            time.sleep(event.press_time)
            base.key_up(event.key_code)
        else:
            base.key_down(event.key_code)
            up_event_list.append(up_event(event.key_code, event.press_time))
