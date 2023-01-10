houses = dict()
count = 0
numhouse = 0
turn = 0

x = 0
y = 0

xr = 0
yr = 0

houses['0.0'] = 1

with open('day_3_data.txt', 'r') as file:
    directions = file.read()

for direct in directions:

    if turn == 0:
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
        turn = 1
        continue

    if turn == 1:
        if direct == '^':
            yr += 1
        if direct == 'v':
            yr -= 1
        if direct == '<':
            xr -= 1
        if direct == '>':
            xr += 1
        posr = (f'{xr}.{yr}')
        houses[posr] = 1
        turn = 0

for house in houses.values():
    numhouse += 1

#numhouse = sum(houses.values())

print(numhouse)