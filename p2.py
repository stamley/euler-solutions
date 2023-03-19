
s = 0

def fibo_4mill(start, second):
    
    if second > 4000000:
        return
    if second % 2 == 0:
        global s
        s += second
    fibo_4mill(second, start + second)

fibo_4mill(1,2)
print(s)
