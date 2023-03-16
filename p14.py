#p14

can = 0

def longest_collatz():
    longest = 1
    number = 1
    global can
    for i in range(1_000_000):
        can = 0
        collatz(i)
        if can > longest:
            longest = can
            number = i
    return number

def collatz_rec(i):
    global can
    if i == 1:
        return
    if i % 2 == 0:
        can += 1
        collatz_rec(i/2)
    else:
        can += 1
        collatz_rec(3*i + 1)

def collatz(i):
    global can
    while i != 1 and i > 0:
        if i % 2 == 0:
            can += 1
            i = i/2
        else:
            can += 1
            i = 3*i + 1


print(longest_collatz())