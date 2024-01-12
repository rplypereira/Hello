import random


stats = ["strength","dexterity","constitution","intelligence","charisma","wisdom"]

def roll(x,y):
    return random.randint(x,y)

def roll_for_stats():
    #Roll 4d6, drop the lowest, return sum
    rolls = [roll(1,6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

def get_stats():
    values = [roll_for_stats() for _ in range(6)]
    c_stats = dict(zip(stats,values))
    sorted_list = sorted(c_stats.items(), key=lambda x:x[1],reverse=True)
    dictionary = dict(sorted_list)
    return dictionary

    


