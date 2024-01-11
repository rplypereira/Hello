import random
import json


#open the .json files and reads their data onto respective variables
with open('names.json','r') as file:
    name_data = json.load(file)
    
classes = ["Barbarian","Bard","Cleric","Druid","Fighter","Monk","Paladin","Ranger","Rogue","Sorcerer","Warlock","Wizard"] #plan on changing it into a .json file with a dictionary for each class
#races = ["Dragonborne","Dwarf","Elf","Half-Elf","Gnome","Halfling","Half-Orc","Human","Tiefling"]
#genders =['female','male']
standard_array = [15,14,13,12,10,8]
stats = ["strength","dexterity","constitution","intelligence","charisma","wisdom"] #plan on changing it into a .json file with a dict for each stat and their characteristics

def c_stats(x,y):
    ''' character stats
        
        -creates a dict by merging the stat and stat value lists
        -returns that dictionary
    '''
    dictionary = dict(zip(x,y))
    return dictionary

def c_name(race, gender):
    '''character name
    
        -creates a list by getting the names from a race based dict on the json file
        -chooses a random name from the list
        -returns that name
    '''
    _list = name_data.get(race,{}).get(gender,[])
    _name = random.choice(_list)
    return _name

def c_gender(name_data):
    """character gender

    Args:
        name_data (json file data): .json file containing race based dictionaries, each with a list of name for male and female gender

    Returns:
        _gender (list.choice) : list of genders from the json file 
    """
    _genders = set()
    for race in name_data.values():
        for gender in race:
            _genders.add(gender)
    _gender_list = list(_genders)
    _gender = random.choice(_gender_list)
    return _gender

def c_class():
    """character class

    Returns:
        _class (list item): choice from the list of classes
    """
    _class = random.choice(classes)
    return _class

def c_race():
    """character race

    Returns:
        race(dictionary key): chooses from the races available in the json file
    """
    races = list(name_data.keys())
    race = random.choice(races)
    return race

if __name__ == "__main__":
    
    """main
    Sets:(randomized)
        gender
        class
        race
        name
        stats
    Returns: 
        .json file containing the character information
    """
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