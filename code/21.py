import math

position = [0, 0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(' ')
    direction, step = movement[0], int(movement[1])
    if direction == 'UP':
        position[1] += step
    elif direction == 'DOWN':
        position[1] -= step
    elif direction == 'LEFT':
        position[0] -= step
    elif direction == 'RIGHT':
        position[0] += step

print(round(math.sqrt(position[0]**2+position[1]**2)))