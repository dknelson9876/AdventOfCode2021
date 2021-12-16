
pos = 0
depth = 0
aim = 0

with open('AdventOfCode/Day2.txt') as f:
    lines = f.readlines()

# for l in lines:
#     # print(line.split())
#     line = l.split()
#     print(line[0])
#     if(line[0] == 'forward'):
#         pos += int(line[1])
#         print(line[1])
#     elif(line[0] == 'down'):
#         depth += int(line[1])
#     elif(line[0] == 'up'):
#         depth -= int(line[1])

for l in lines:
    line = l.split()
    if(line[0] == 'forward'):
        pos += int(line[1])
        depth += aim*int(line[1])
    elif(line[0] == 'down'):
        aim += int(line[1])
    elif(line[0] == 'up'):
        aim -= int(line[1])

print(pos)
print(depth)
print(pos*depth)