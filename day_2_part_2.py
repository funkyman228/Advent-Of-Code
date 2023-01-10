import sys

def secsmall(nums):
    nums.sort()
    return nums[1]

def mul(nums):
    mnums = nums[0]
    skip = 1
    for num in nums:
        if skip == 1:
            skip = 0
            continue
        mnums = mnums * num
    return mnums

count = 0
sides = [0,0,0]
area = 0
tribbon = 0

with open('day_2_data.txt', 'r') as file:
    presents = file.readlines()

for line in presents:
    presents[count] = line.strip()
    count += 1

for present in presents:
    presentdime = present.split('x')

    presentdime[0] = int(presentdime[0])
    presentdime[1] = int(presentdime[1])
    presentdime[2] = int(presentdime[2])

    length = presentdime[0]
    width = presentdime[1]
    height = presentdime[2]


    sides[0] = length * width
    sides[1] = length * height
    sides[2] = width * height
    
    extra = min(sides)
    print(present)

    area += sum(sides) * 2 + extra
    print(area)

    tribbon += (min(presentdime)*2)+(secsmall(presentdime)*2)+(mul(presentdime))
    print(tribbon)

print('\n\n\n')
print(f'paper = {area}')
print(f'ribbon = {tribbon}')
