with open('AdventOfCode2021\day6\day6.txt') as f:
    line = f.readlines()[0]

t = 256
input = [eval(i) for i in line.split(',')]
print(f"Initial State: {input}")

def rotate_portion_left(arr, startIndex, endIndex):
    temp = arr[startIndex]
    for i in range(startIndex, endIndex):
        arr[i] = arr[i+1]
    arr[endIndex] = temp

# old code - not fast enough
# totalNewSquid = 0
# for i in range(t):
#     # decrement every element of arr by 1
#     newSquid = 0
#     arr = [num-1 for num in arr]
#     # arr = list(map(lambda x: x-1, arr))
#     for index, num in enumerate(arr):
#         if num == -1:
#             arr[index] = 6
#             newSquid += 1
#     if newSquid > 0:
#         newSquids = [8] * newSquid
#         # arr.extend(newSquids)
#     totalNewSquid += newSquid
#     print(f"After \t{i+1} days: {arr}\tCalculated: {((i-3) // 7) + 1}")
#     # print(i)
# print(f"Count: {len(input)}")

# def get_squid_spawned(internal_timer, days_in_cycle):
#     print()

fishCounts = [0] * 9
for num in input:
    fishCounts[num] += 1

for i in range(t):
    # shift elements left by one, subtracting one day from each fish
    new6 = fishCounts[0]
    fishCounts[0] = 0
    fishCounts.append(fishCounts.pop(0))
    fishCounts[6] += new6
    # rotate_portion_left(fishCounts, 0, 6)
    # for every fish that just reset its internal timer, spawn a new fish
    fishCounts[8] += new6
    print(f"After \t{i+1} days: {fishCounts}")

print(sum(fishCounts))
