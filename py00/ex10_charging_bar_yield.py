from time import sleep
import time

def ft_fill(bar, n, sens):
    if len(bar) > n:
        bar = bar[:n]
    if sens == 1:
        while len(bar) < n:
            bar += ' '
        return bar
    else:
        ret = ''
        i = 0
        while len(bar) + i< n:
            ret += ' '
            i += 1
        ret += bar
        return ret

def ft_progress(lst):
    for i in lst:
        yield i

start_time = time.time()
lst = range(500)
bar = '>'
time_sleep = 0.05
ETA = time_sleep * len(lst)
lastper = 0
for elem in ft_progress(lst):
    per = (elem / lst[-1] * 100)
    strper = "{:.0f}".format(per)
    strper = ft_fill(strper, 3, 0)
    if per - lastper > 2:
        bar = '=' + bar
        lastper = per
    if elem == lst[-1]:
        bar = '=' + bar
    print(f"ETA: {ETA}s [{strper}%][{ft_fill(bar, 50, 1)}] {elem}/{lst[-1]} | {time.time() - start_time:.2f}s", end='\r', flush=True)
    sleep(time_sleep)
print()