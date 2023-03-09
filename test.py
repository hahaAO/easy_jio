import executor
import base


print(executor.scan_time)


def SKILL_Q(press_time, wait):
    a = executor.key_event()
    a.key_code = base.key_q
    a.press_time = press_time
    a.wait = wait
    executor.event_list.append(a)

SKILL_Q()

print(executor.total_time())
executor.execute()

