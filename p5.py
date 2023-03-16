# p5

import time

def smallest():
    for i in range(20,400000000,20):
        for j in range(1,21):
            if i % j == 0 and j == 20:
                return i
            if i % j != 0:
                break
    print("none")
st = time.process_time()
smallest()
el_time = time.process_time() - st
print(el_time)