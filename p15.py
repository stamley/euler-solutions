#p15
# Test all paths in a 20x20 grid only being able to move right and down

# This problem is solved using combinatorics
# The answer is equal to 40 chooses 20

paths = 0

def lattice(right, down):
    global paths
    if right < 0 or down < 0:
        return
    elif right == 0 and down == 0:
        paths += 1
        return
    else:
        lattice(right-1, down)
        lattice(right, down-1)

lattice(20,20)

print(paths)
