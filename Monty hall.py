#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def out(*args):
    print(*args, end='')
def play(switch):
    doors = ['car', 'banana', 'banana']
    random.shuffle(doors)
    choose = random.choice([0, 1, 2])
    out('player chooses door {}; '.format(choose))

    # The host now opens one of the unchosen doors that contains banana.
    show = random.choice([x for x in [0, 1, 2] if x != choose and
                                                  doors[x] == 'banana'])
    out('host shows door {} has banana; '.format(show))

    if switch:
        # The player switches to the other remaining door.
        choose = [x for x in [0, 1, 2] if x not in [choose, show]][0]
        out('player switches to door {}; '.format(choose))
    else:
        # The player does not switch.
        out('player sticks with door {}; '.format(choose))

    # Host opens the chosen door and declares ther result.
    out('door {} has {}; '.format(choose, doors[choose]))
    win = doors[choose] == 'car'
    out('player {}!'.format('wins' if win else 'loses'))
    print()
    return win

if __name__ == '__main__':
    games = 1000 # Number of times to play the game

    # Simulation 1: Player never switches door
    print('Simulation 1: No Switching')
    wins = 0
    for _ in range(games):
        if play(False):
            wins += 1
    success_rate_1 = wins / games
    print()


# In[3]:



    # Simulation 2: Player always switches
    print('Simulation 1: Always Switching')
    wins = 0
    for _ in range(games):
        if play(True):
            wins += 1
    success_rate_2 = wins / games
    print()


# In[4]:


print('success rate without switching: {:.2f}'.format(success_rate_1))
print('success rate *with*  switching: {:.2f}'.format(success_rate_2))


# In[ ]:




