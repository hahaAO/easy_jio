import executor
import base
import time



def SKILL_Q(press_time, wait=True):
    a = executor.key_event()
    a.key_code = base.key_q
    a.press_time = press_time
    a.wait = wait
    executor.event_list.append(a)

def SKILL_W(press_time, wait=True):
    a = executor.key_event()
    a.key_code = base.key_w
    a.press_time = press_time
    a.wait = wait
    executor.event_list.append(a)


SKILL_Q(2)
SKILL_W(1,False)


t1 = time.time()
# executor.execute()
t2 = time.time()
print("Predict time cost",executor.total_time())
print("real time cost: ", t2-t1)
