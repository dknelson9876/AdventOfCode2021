with open('AdventOfCode/Day3.txt') as f:
    lines = f.readlines()

for i, val in enumerate(lines):
    lines[i] = val.strip()

# Set the length of count to the length of a single line
# count = [0] * len(lines[0])

# for line in lines:
#     for i, val in enumerate(line):
#         if(val == "1"):
#             count[i] += 1

# print(count)

# gamma = ""
# epsilon = ""

# for i in count:
#     if(float(i/len(lines)) >= .5):
#         gamma += "1"
#         epsilon += "0"
#     else:
#         gamma += "0"
#         epsilon += "1"

# print(gamma)
# print(epsilon)
# print(int(gamma, 2) * int(epsilon, 2))


arr = lines.copy()

i = 0
while len(arr) > 1:
    count = 0
    for val in arr:
        if val[i] == "1":
            count += 1
    
    newArr = []

    if float(count/len(arr)) >= .5:
        # 1 is more common, remove 0's
        for val in arr:
            if val[i] == "1":
                newArr.append(val)
    else:
        for val in arr:
            if val[i] == "0":
                newArr.append(val)
    arr = newArr
    i += 1

ogr = arr[0]

arr = lines.copy()

i = 0
while len(arr) > 1:
    count = 0
    for val in arr:
        if val[i] == "1":
            count += 1
    
    newArr = []

    if float(count/len(arr)) >= .5:
        # 1 is more common, remove 0's
        for val in arr:
            if val[i] == "0":
                newArr.append(val)
    else:
        for val in arr:
            if val[i] == "1":
                newArr.append(val)
    arr = newArr
    i += 1

co2 = arr[0]

print(ogr)
print(co2)
print(int(ogr, 2) * int(co2, 2))

