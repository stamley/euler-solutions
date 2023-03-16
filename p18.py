#p18

# Using readlines()
file1 = open('p18.txt', 'r')
lines = file1.readlines()
  
# Strips the newline character
rows = []
for line in lines:
    rows.append(line.split())

m = 0
p = []
def max_path(row, index, path, steps: list):
    global m
    global p
    if row == 15: 
        if path > m: 
            m = path
            p = steps
        return
    path += int(rows[row][index])
    max_path(row+1, index, path, steps + [(row+1, index, int(rows[row][index]))])
    max_path(row+1, index+1, path, steps + [(row+1, index+1, int(rows[row][index]))])

max_path(0,0,0, [])
print(m, p)