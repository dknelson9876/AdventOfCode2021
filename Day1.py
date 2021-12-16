
with open('AdventOfCode/Day1_1.txt') as f:
    lines = f.readlines()

count = 0

values = []
for line in lines:
    values.append(int(line))

# print(type(values[0]))

# for i in range(len(values)-1):
#     if(values[i] < values[i+1]):
#         count += 1

for i in range(len(values)-3):
    sumA = values[i]+values[i+1]+values[i+2]
    sumB = values[i+1] + values[i+2] + values[i+3]
    if(sumA < sumB):
        count += 1

print(count)
f.close()