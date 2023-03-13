import base
import time

# 计算机从键盘上扫走一次key_down或key_up需要的时间
# 这个数据是不停往键盘芯片塞扫描码测出来的，实际上因为真正的脚本有sleep的操作
# 芯片在不忙碌的情况下延迟会更低，所以略高的预测值不影响实际运行
scan_time = 0.0044

# 用来标记暂停时间的操作，并不存在这个键盘扫描码
sleep_key = 0x9999


class key_event:
    key_code: int
    wait = True
    press_time: int


class up_event:
    key_code: int
    delay_time: float  # 异步地延迟多少秒后抬起该按键


game_time = 0.0

_event_list = []

def append_event(k_e:key_event):
    new_k_e =  key_event()
    new_k_e.key_code = k_e.key_code
    new_k_e.wait = k_e.wait
    new_k_e.press_time = k_e.press_time
    
    _event_list.append( new_k_e)

    


# 获取最近要抬起的键


def get_closest_event(event_list: list):
    if len(event_list) == 0:
        return None
    else:
        tmp = event_list[0]
        for i in range(1, len(event_list)):
            if tmp.delay_time > event_list[i].delay_time:
                tmp = event_list[i]
        return tmp

# 刷新异步等待的抬起事件时间


def flow(event_list: list, time: float):
    for tmp in event_list:
        tmp.delay_time -= time


def sleep(time: float):
    tmp = key_event()
    tmp.key_code = sleep_key
    tmp.press_time = time
    tmp.wait = True
    _event_list.append(tmp)

# 计算执行完所有按键需要的时间


def total_time():
    global game_time
    for event in _event_list:
        if (event.key_code != sleep_key):
            game_time += 2*scan_time
        if (event.wait):
            game_time += event.press_time
    return game_time


def timesleep(t: float):
    if t > 0:
        time.sleep(t)
    else:
        pass

# 真正执行按键操作
def execute():
    up_event_list = []  # 已按下\等待抬起的事件,每次 down,up,sleep 都要 flow
    for event in _event_list:
        while True:  # 如果一直有延迟的抬起就不断执行
            closest_event = get_closest_event(up_event_list)
            if (closest_event != None and closest_event.delay_time < scan_time):
                timesleep(closest_event.delay_time)
                base.key_up(closest_event.key_code)
                up_event_list.remove(closest_event)
                flow(up_event_list, closest_event.delay_time+scan_time)
            else:
                break
        if (event.wait):
            event_tmp = key_event()  # 使用临时变量，避免执行过程改变原本设定的值
            event_tmp.key_code = event.key_code
            event_tmp.press_time = event.press_time
            event_tmp.wait = event.wait

            if event_tmp.key_code != sleep_key:
                base.key_down(event_tmp.key_code)
                flow(up_event_list, scan_time)
            while True:  # 如果一直有延迟的抬起就不断执行
                closest_event = get_closest_event(up_event_list)
                if (closest_event != None and closest_event.delay_time < event_tmp.press_time):
                    timesleep(closest_event.delay_time)
                    base.key_up(closest_event.key_code)
                    up_event_list.remove(closest_event)
                    flow(up_event_list, closest_event.delay_time+scan_time)
                    event_tmp.press_time -= (closest_event.delay_time+scan_time)
                else:
                    break
            timesleep(event_tmp.press_time)
            flow(up_event_list, event_tmp.press_time)
            if event_tmp.key_code != sleep_key:
                base.key_up(event_tmp.key_code)
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
