n = int(input())
total_free_chairs = 0
visited = False

for day in range(1, n + 1):
    current =  input().split()
    chair_in_hall = len(current[0])
    count_chairs = int(current[1])

    if chair_in_hall < count_chairs:
        visited = True
        needed_chairs_in_room = count_chairs - chair_in_hall
        print(f'{needed_chairs_in_room} more chairs needed in room {day}')
    else:
        total_free_chairs += chair_in_hall - count_chairs

if not visited:
    print(f'Game On, {total_free_chairs} free chairs left')