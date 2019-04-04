import time

current_milli_time = lambda: int(round(time.time() * 1000))


def get_week():
    return time.strftime("%A",time.localtime())