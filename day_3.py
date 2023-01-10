houses = dict()
count = 0
numhouse = 1

x = 0
y = 0

with open('day_3_data.txt', 'r') as file:
    directions = file.read()

for direct in directions:
    if direct == '^':
        y += 1
    if direct == 'v':
        y -= 1
    if direct == '<':
        x -= 1
    if direct == '>':
        x += 1
    pos = (f'{x}.{y}')
    houses[pos] = 1

for house in houses.values():
    numhouse += 1

#numhouse = sum(houses.values())

print(numhouse)