#p22
names = []

file1 = open('p22_names.txt', 'r')
lines = file1.readlines()
  
# Strips the newline character
rows = []
for line in lines:
    row = line.split(",")
    for name in row:
        name = name[1:]
        name = name[:len(name)-1]
        #print(name)
        rows.append(name)

rows = sorted(rows)

total = 0

for i in range(len(rows)):
    name = rows[i]
    points = 0
    for c in name:
        points += ord(c) - 64
    total += points * (i + 1)

print(total)