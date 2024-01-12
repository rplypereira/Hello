import random
import json
import stats
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

with open("names.json","r") as f:
    n_data = json.load(f)
        
with open("classes.json", "r") as file:
    class_data = json.load(file)


GENDERS = ['Male', 'Female']
class Character:
    def __init__(self):
        self.gender = random.choice(GENDERS)
        self.race = self. generate_race()
        self.name = self.generate_name()
        self.char_class = self.generate_class()
        self.stats = stats.get_stats()
        self.modifiers = self.generate_modifiers(self.stats)
        self.hp = self.generate_hp()
        self.ac = self.generate_ac()
        
    
    def generate_race(self):
        return random.choice(list(n_data.keys()))
    
    def generate_name(self):
        return random.choice(n_data[self.race][self.gender])

    def generate_class(self):
        selected_class = random.choice(list(class_data.keys()))
        class_attrs = class_data[selected_class]
        
        self.hit_die = class_attrs["hit_die"]
        self.primary_ability = class_attrs["primary_ability"]
        self.saving_throw_proficiencies = class_attrs["saving_throw_proficiencies"]
        self.armor_proficiencies = class_attrs["armor_proficiencies"]
        self.weapon_proficiencies = class_attrs["weapon_proficiencies"]
        self.skill_proficiencies = class_attrs["skill_proficiencies"]
        self.starting_equipment = class_attrs["starting_equipment"]
        self.features = class_attrs["features"]
        self.modifiers = class_attrs["modifiers"]
    
        return selected_class
    
    def generate_modifiers(self, stats):
        return {stat: (value - 10) // 2 for stat, value in stats.items()}
    
    def generate_hp(self):
        base_hp = int(self.hit_die[1:])
        const_modifier = self.modifiers.get('Constitution', 0)
        return max(base_hp + const_modifier, 1)
        
    def generate_ac(self):
        return 10 + self.modifiers.get('Dexterity', 0)  
    
    
    def to_dict(self):      
        return vars(self)  
    
    def save_to_file(self, file_path):
        try:
            char_dict = self.to_dict()
            with open(file_path, 'w') as file:
                json.dump(char_dict, file, indent=4)
        except IOError as e:
            print(f"An error occurred while writing to {file_path}: {e}")
            
    def generate_pdf(self, filename):
        c = canvas.Canvas(filename, pagesize=letter)
        c.drawString(50, 750, f'Name: {self.name}')
        c.drawString(50, 735, f'Race: {self.race}')
        c.drawString(50, 720, f'Gender: {self.gender}')
        c.drawString(50, 705, f'Class: {self.char_class}')
        c.drawString(50, 690, 'Stats:')
        c.drawString(65,675,f"-Strength: {self.stats['strength']} : ({self.modifiers['strength']})")
        c.drawString(65,660,f"-Dexterity: {self.stats['dexterity']} : ({self.modifiers['dexterity']})")
        c.drawString(65,645,f"-Charisma: {self.stats['charisma']} : ({self.modifiers['charisma']})")
        c.drawString(180,675,f"-Constitution: {self.stats['constitution']} : ({self.modifiers['constitution']})")
        c.drawString(180,660,f"-Intelligence: {self.stats['intelligence']} : ({self.modifiers['intelligence']})")
        c.drawString(180,645,f"-Wisdom: {self.stats['wisdom']} : ({self.modifiers['wisdom']})")
        c.drawString(50,630,f"Primary ability: {str(self.primary_ability)}")
        c.drawString(50,615,f"Saving throws: {self.saving_throw_proficiencies}")
        c.drawString(300, 750, f'Hit Die: {self.hit_die}')
        c.drawString(50,600, f"Weapon proficiency: ")
        c.drawString(65,585,f"{self.weapon_proficiencies}")
        c.drawString(50,570,f"Armour proficiencies: ")
        c.drawString(65,555,f"{self.armor_proficiencies}")
        c.drawString(50, 540, f'HP: {self.hp}')
        c.drawString(50, 525, f'AC: {self.ac}')
        c.drawString(50,510,f"Skill proficiencies: ")
        c.drawString(50,495,f"{self.skill_proficiencies}")
        

        # Can do more formatting and drawing as needed
        # ...

        c.save()


if __name__ == "__main__":
    character = Character()
    #character.save_to_file(character.name+'.json')#character.name+
    character.generate_pdf(f"character.pdf")#{character.name.replace(' ','_')}
    