import random
import json

with open('names.json','r') as file:
    name_data = json.load(file)
    
classes = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"]
#races = ["Dragonborne","Dwarf","Elf","Half-Elf","Gnome","Halfling","Half-Orc","Human","Tiefling"]
#genders =['female','male']
standard_array = [15,14,13,12,10,8]
stats = ["strength","dexterity","constitution","intelligence","charisma","wisdom"]

def c_stats(x,y):
    dictionary = dict(zip(x,y))
    return dictionary

def c_name(race, gender):
    _list = name_data.get(race,{}).get(gender,[])
    _name = random.choice(_list)
    return _name

def c_gender(name_data):
    _genders = set()
    for race in name_data.values():
        for gender in race:
            _genders.add(gender)
    _gender_list = list(_genders)
    _gender = random.choice(_gender_list)
    return _gender

def c_class():
    _class = random.choice(classes)
    return _class

def c_race():
    races = list(name_data.keys())
    race = random.choice(races)
    return race

if __name__ == "__main__":
    character_gender = c_gender(name_data)
    character_class = c_class()
    character_race = c_race()
    character_name = c_name(character_race,character_gender)
    stat_name = stats
    stat_values = random.sample(standard_array,len(standard_array))
    character_stats = c_stats(stat_name,stat_values)
    character = {"name":character_name,"gender":character_gender,"class":character_class,"race":character_race,"stats":character_stats}
    
    #f_name = character_name+".json" 
    with open("test.json",'w') as wf:
        json.dump(character,wf)