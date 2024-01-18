from googleapiclient.discovery import build

api_key = "AIzaSyCQGY9gWZzeaKYgRbSVPs9R9ji_teOOkyw"
search_engine_id = "6456ce472f50f4fa3"

query = "Polymorphism explained"

service = build("customsearch","v1",developerKey=api_key)
res = service.cse().list(q = query,cx = search_engine_id,).execute()

for item in res['items']:
    print(item['title'],item['link'])


class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "bark!"
    
class Cat(Animal):
    def speak(self):
        return "meow!"
    

# Using polymorphism to handle complexity
animals = [Dog(),Cat()]
for animal in animals:
    print(animal.speak())