import executor
import base
import time


def Left_shun(press_time=0.18):
    tmp = executor.key_event()
    tmp.key_code = base.key_Left
    tmp.press_time = 0.16
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.13)

    tmp.key_code = base.key_LAlt
    tmp.press_time = press_time
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.18)


def Right_shun(press_time=0.18):
    tmp = executor.key_event()
    tmp.key_code = base.key_Right
    tmp.press_time = 0.16
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.13)

    tmp.key_code = base.key_LAlt
    tmp.press_time = press_time
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.18)


def Right_walk(press_time):
    tmp = executor.key_event()
    tmp.key_code = base.key_Right
    tmp.press_time = press_time
    tmp.wait = True
    executor.event_list.append(tmp)


def Left_walk(press_time):
    tmp = executor.key_event()
    tmp.key_code = base.key_Left
    tmp.press_time = press_time
    tmp.wait = True
    executor.event_list.append(tmp)


def Up_shun():
    tmp = executor.key_event()
    tmp.key_code = base.key_UpArrow
    tmp.press_time = 0.16
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.13)

    tmp.key_code = base.key_LAlt
    tmp.press_time = 0.2
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.18)


def Down_shun():
    tmp = executor.key_event()
    tmp.key_code = base.key_DownArrow
    tmp.press_time = 0.16
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.13)

    tmp.key_code = base.key_LAlt
    tmp.press_time = 0.2
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.18)


def Left_jump(press_time=0.12):
    tmp = executor.key_event()
    tmp.key_code = base.key_Left
    tmp.press_time = 0.36
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.08)

    tmp.key_code = base.key_space
    tmp.press_time = press_time
    tmp.wait = True
    executor.event_list.append(tmp)


def Right_jump(press_time=0.12):
    tmp = executor.key_event()
    tmp.key_code = base.key_Right
    tmp.press_time = 0.36
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.08)

    tmp.key_code = base.key_space
    tmp.press_time = press_time
    tmp.wait = True
    executor.event_list.append(tmp)


def Left_duan_shun():
    tmp = executor.key_event()
    tmp.key_code = base.key_Left
    tmp.press_time = 0.09
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.03)

    tmp.key_code = base.key_LAlt
    tmp.press_time = 0.03
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.25)


def erda_shower():
    tmp = executor.key_event()
    tmp.key_code = base.key_DownArrow
    tmp.press_time = 0.39
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.13)

    tmp.key_code = base.key_LShift
    tmp.press_time = 0.13
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.18)


def altar():
    tmp = executor.key_event()
    tmp.key_code = base.key_DownArrow
    tmp.press_time = 0.39
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.13)

    tmp.key_code = base.key_LCtrl
    tmp.press_time = 0.13
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.13)


def JQQQ():
    tmp = executor.key_event()
    tmp.key_code = base.key_q
    tmp.press_time = 0.13
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.02)


def JWWW():
    tmp = executor.key_event()
    tmp.key_code = base.key_w
    tmp.press_time = 0.15
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.14)


def JEEE():
    tmp = executor.key_event()
    tmp.key_code = base.key_e
    tmp.press_time = 0.15
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.14)


def J111():
    tmp = executor.key_event()
    tmp.key_code = base.key_1
    tmp.press_time = 0.6
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.3)


def J222():
    tmp = executor.key_event()
    tmp.key_code = base.key_2
    tmp.press_time = 0.12
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.3)


def J444():
    tmp = executor.key_event()
    tmp.key_code = base.key_4
    tmp.press_time = 0.22
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.3)


def J333():
    tmp = executor.key_event()
    tmp.key_code = base.key_3
    tmp.press_time = 0.2
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.1)


def JRRR():
    executor.sleep(0.2)
    tmp = executor.key_event()
    tmp.key_code = base.key_r
    tmp.press_time = 0.02
    tmp.wait = True
    executor.event_list.append(tmp)


def Jttt():
    tmp = executor.key_event()
    tmp.key_code = base.key_t
    tmp.press_time = 0.3
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.2)


def Jdel():
    tmp = executor.key_event()
    tmp.key_code = base.key_del
    tmp.press_time = 0.3
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.2)


def JINS():
    tmp = executor.key_event()
    tmp.key_code = base.key_ins
    tmp.press_time = 0.3
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.45)


def JPGUP():
    tmp = executor.key_event()
    tmp.key_code = base.key_PGUP
    tmp.press_time = 0.3
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.25)


def R_S_A():
    tmp = executor.key_event()
    tmp.key_code = base.key_Right
    tmp.press_time = 0.08
    tmp.wait = True
    executor.event_list.append(tmp)

    JRRR()
    JQQQ()
    Right_shun()


def L_S_A():
    tmp = executor.key_event()
    tmp.key_code = base.key_Left
    tmp.press_time = 0.08
    tmp.wait = True
    executor.event_list.append(tmp)
    JRRR()
    JQQQ()
    Left_shun()


def F10():
    tmp = executor.key_event()
    tmp.key_code = base.key_F10
    tmp.press_time = 0.18
    tmp.wait = True
    executor.event_list.append(tmp)


def UP_L_Q():
    tmp = executor.key_event()
    tmp.key_code = base.key_UpArrow
    tmp.press_time = 0.29
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.13)

    tmp.key_code = base.key_LAlt
    tmp.press_time = 0.04
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.04)

    tmp.key_code = base.key_Left
    tmp.press_time = 0.4
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.09)

    tmp.key_code = base.key_q
    tmp.press_time = 0.2
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.43)

    tmp.key_code = base.key_q
    tmp.press_time = 0.2
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.2)


def UP_R_Q():
    tmp = executor.key_event()
    tmp.key_code = base.key_UpArrow
    tmp.press_time = 0.29
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.13)

    tmp.key_code = base.key_LAlt
    tmp.press_time = 0.04
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.04)

    tmp.key_code = base.key_Right
    tmp.press_time = 0.4
    tmp.wait = False
    executor.event_list.append(tmp)
    executor.sleep(0.09)

    tmp.key_code = base.key_q
    tmp.press_time = 0.2
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.43)

    tmp.key_code = base.key_q
    tmp.press_time = 0.2
    tmp.wait = True
    executor.event_list.append(tmp)
    executor.sleep(0.2)


def sx_q(time=2):
    while time > 0:
        # 10 轮 21.601 秒
        UP_L_Q()
        UP_R_Q()
        time -= 1


def R_QING(i=4):
    while i > 0:
        # 4 轮 8 秒
        UP_R_Q()
        if i != 1:
            Right_shun(0.27)
        i -= 1


print("启动，等待5s")


time.sleep(5)


# print(executor.total_time())
# exit()

Left_shun()
Right_walk(0.13)
Right_shun()
J222()
F10()
Right_shun()
JEEE()
Right_shun()
JWWW()
Right_shun()
JQQQ()
Right_shun()
altar()
Right_shun()
erda_shower()
Left_walk(0.12)
Left_shun()
Jttt()
executor.sleep(0.2)

# 站点 1
sx_q(3)
UP_L_Q()
executor.sleep(0.3)
JEEE()
executor.sleep(0.2)
sx_q(2)
Left_shun()
JWWW()
Right_shun()
executor.sleep(0.2)
sx_q(3)
executor.sleep(0.3)
Jttt()
executor.sleep(0.2)
sx_q(1)
Left_shun()
JEEE()
Right_shun()
executor.sleep(0.2)
sx_q(1)
executor.sleep(0.2)
J444()
Right_shun()
JWWW()
Left_shun()
sx_q(1)
executor.sleep(0.2)
JEEE()

# 掉左边

Down_shun()
Jdel()
executor.sleep(0.3)
F10()
Left_walk(0.28)
Down_shun()
executor.sleep(0.1)
R_QING(4)
F10()
Right_shun()
altar()
R_QING(2)


Down_shun()


executor.sleep(0.3)
JPGUP()
F10()
Left_walk(0.28)
Down_shun()
executor.sleep(0.1)
R_QING(4)
F10()
Right_shun()
JEEE()
Right_shun()
executor.sleep(0.1)
R_QING(1)

Down_shun()

executor.sleep(0.3)
JINS()
F10()
Left_walk(0.28)
Down_shun()
executor.sleep(0.1)
R_QING(4)
Right_shun()
JEEE()
Right_shun()
executor.sleep(0.2)
Up_shun()
executor.sleep(0.2)
Jttt()
Down_shun()
executor.sleep(0.1)
F10()

Down_shun()
executor.sleep(0.8)
F10()
Left_walk(0.28)
Down_shun()
executor.sleep(0.1)
R_QING(4)
F10()
Right_shun()
JEEE()
Right_shun()
executor.sleep(0.1)
J444()
Down_shun()
executor.sleep(0.8)
F10()
Down_shun()
JQQQ()

T1 = time.time()
executor.execute()
T2 = time.time()
print('程序实际运行时间:%s秒' % ((T2 - T1)))
print('程序预测运行时间: ', executor.total_time())
