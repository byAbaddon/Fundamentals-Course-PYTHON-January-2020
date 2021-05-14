lost_fight = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

count_broken_shield = 0
money = 0

for day in range(1, lost_fight + 1):
    if day % 2 == 0:
        money += helmet

    if day % 3 == 0:
        money += sword

    if day % 2 == 0 and day % 3 == 0:
        money += shield
        count_broken_shield += 1
        if count_broken_shield == 2:
            money += armor
            count_broken_shield = 0


print(f'Gladiator expenses: {money:.2f} aureus')