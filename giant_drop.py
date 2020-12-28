import random
import Classes
def giant_reward(victory):
    drop = 0
    if victory:
        reward = random.choice([4, 5, 6])
        if reward == 1:
            drop = Classes.Energy()
        elif reward == 2:
            drop = Classes.Fatall()
        elif reward == 3:
            drop = Classes.Swift()
        elif reward == 4:
            drop = Classes.Guard()
        elif reward == 5:
            drop = Classes.Angel()
        elif reward == 6:
            drop = Classes.Beast()
        return drop
    else:
        return 'You lose'

