#p25

s = 0
index = 0

def fibo_4mill(start, second):
    global s, index
    
    if len(str(s)) > 1000:
        return
    
    index += 1
    s += second
    fibo_4mill(second, start + second)

fibo_4mill(89,144)
print(s, index)