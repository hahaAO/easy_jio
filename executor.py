import base
import time

# 计算机从键盘上扫走一次key_down或key_up需要的时间
scan_time = 0.0044

# 用来标记暂停时间的操作，并不存在这个键盘扫描码
sleep_key = 0x9999

class key_event:
    key_code: int
    wait = True
    press_time: int


class up_event:
    key_code: int
    delay_time: float


game_time = 0.0

event_list = []


def get_closest_event(event_list: list):
    if len(event_list) == 0:
        return None
    else:
        tmp = event_list[0]
        for i in range(1, len(event_list)):
            if tmp.delay_time > event_list[i].delay_time:
                tmp = event_list[i]
        return tmp


def flow(event_list: list, time: float):
    for tmp in event_list:
        tmp.delay_time -= time


def sleep(time:float):
    tmp = key_event()
    tmp.key_code = sleep_key
    tmp.press_time = time
    tmp.wait = True
    event_list.append(tmp)


def total_time():
    global game_time
    for event in event_list:
        game_time += 2*scan_time
        if (event.wait):
            game_time += event.press_time
    return game_time


def execute():
    up_event_list = []  # 已按下等待抬起的事件 , 每次down，up,sleep 都要 flow
    for event in event_list:
        while True: # 如果一直有延迟的抬起就不断执行
            closest_event = get_closest_event(up_event_list)
            if (closest_event != None and closest_event.delay_time < scan_time):
                time.sleep(closest_event.delay_time)
                base.key_up(closest_event.key_code)
                up_event_list.remove(closest_event)
                flow(up_event_list, closest_event.delay_time+scan_time)
            else:
                break
        if (event.wait):
            # TODO execute up_event
            if event.key_code != sleep_key:
                base.key_down(event.key_code)
                flow(up_event_list,scan_time)
            while True: # 如果一直有延迟的抬起就不断执行
                closest_event = get_closest_event(up_event_list)
                if (closest_event != None and closest_event.delay_time < event.press_time):
                    time.sleep(closest_event.delay_time)
                    base.key_up(closest_event.key_code)
                    up_event_list.remove(closest_event)
                    flow(up_event_list, closest_event.delay_time+scan_time)
                    event.press_time -= (closest_event.delay_time+scan_time)
                else:
                    break
            time.sleep(event.press_time)
            flow(up_event_list, event.press_time)
            if event.key_code != sleep_key:
                base.key_up(event.key_code)
                flow(up_event_list, scan_time)
        else:
            # 这个事件的抬起动作要延迟执行
            if event.key_code == sleep_key:
                print("delay event can not be sleep!")
                exit()
            base.key_down(event.key_code)
            tmp = up_event()
            tmp.key_code = event.key_code
            tmp.delay_time = event.press_time
            up_event_list.append(tmp)
            flow(up_event_list, scan_time)
