import Classes
import giant_drop
import random
vic = random.choice([0, 1])
rune = giant_drop.giant_reward(vic)
if rune == 'You lose':
    print(rune)
else:
    print(rune)
    print(rune.name)
    print(rune.level)
    rune.grade()
    for i in range(20):
        rune.grade()
    print(rune.level)
    print(rune.attack)
    rune.attack+=100
    print(rune.attack)
    print(rune.mainstat)
