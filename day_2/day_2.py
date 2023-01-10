import sys

count = 0
sides = [0,0,0]
area = 0

with open('day_2_data.txt', 'r') as file:
    presents = file.readlines()

for line in presents:
    presents[count] = line.strip()
    count += 1

for present in presents:
    presentdime = present.split('x')
    length = int(presentdime[0])
    width = int(presentdime[1])
    height = int(presentdime[2])


    sides[0] = length * width
    sides[1] = length * height
    sides[2] = width * height
    
    extra = min(sides)
    print(present)

    area += sum(sides) * 2 + extra
    print(area)


print('\n\n\n')
print(area)
