# Animal.py
# by Russell Flory
# created 2-19-2024

class Animal:
    has_brain = True
    is_alive = True
    age = 0
    name = None

    def move(self, speed, direction, distance):
        pass

class Bird(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def chirp(self):
        print("""
   \\\\     _______________
   (o>   /  CHIRP CHIRP  \\
\\\_//)   \\_______________/
 \\_/_)
  _|_      
""")


billy = Bird("billy", 16)
print(f"This is {billy.name}, he is {billy.age} years old")
print("Isn't he cute?! Listen to him chirp chirp.")
billy.chirp()