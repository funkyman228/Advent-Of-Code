with open('day_1_data.txt', 'r') as file:
    hotel = file.read()

cfloor = 0
count = 0


for floori in range(len(hotel)):
    floor = hotel[floori]
    if floor == '(':
        cfloor += 1
    elif floor == ')':
        cfloor -= 1
    else:
        print('error')
    count += 1
    print(cfloor, floor, count)
    if cfloor < 0:
        print(count)
        input()

print('\n')
print('awnser =', cfloor)