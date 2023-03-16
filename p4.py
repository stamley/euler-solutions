
# p4

import time

# start with a = 100 and b = 100
# check if product is palindrome
# set it to max if it is
# increase b with 1 and repeat process.
# when b reaches 999, increase a with 1.
# ~800 000 iterations, might be too much

def palindrome():
    largest = 1
    a, b = 0,0
    for i in range(100,999):
        for j in range(100,999):
            p = i * j
            if is_pal(p) and p > largest:
                largest = p
                a,b = i,j

    return (largest,a,b)

def is_pal(num):
    n = str(num)
    f_half = n[:len(n)//2]
    s_half = ""
    if len(n) % 2 == 0:
        s_half = n[len(n)//2:]
    else:
        # Disregard the middle digit
        # since it is irrelevant for 
        # palindrome
        s_half = n[len(n)//2+1:]
    # Reverse string
    s_half = s_half[::-1]
    if f_half == s_half:
        return True
    else:
        return False

#print("1: ",n[:len(n)//2])
#print("2: ",n[len(n)//2:])
st = time.process_time()
palindrome()
el_time = time.process_time() - st
print(st)