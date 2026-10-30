# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name,"is eating.")

    def make_sound(self):
        print(self.name, "makes a sound")

# Child classes override the inherited method make_sound()
class Lion(Animal):
    def make_sound(self):
        print(self.name, "roars loudly!")

    def eat(self):
        print(self.name,"eats fresh meat.")


class Elephant(Animal):
    def make_sound(self):
        print(self.name, "trumpets!")

    def eat(self):
        print(self.name,"eats grass and fruits.")

class Monkey(Animal):
    def make_sound(self):
        if self.name == "George":                                           #intellisense autocompleted lines 30-33, and lines 36-39
            print(self.name, "says 'Ooh Ooh Ah Ah!' and dances around while the Man in the Yellow Hat says 'Oh, George! There yo u are!'")
        else:
            print(self.name, "chatters!")

    def eat(self):
        if self.name == "George":
            print(self.name,"eats bananas, vegetables, and Chef Pisghetti's spaghetti.")
        else:
            print(self.name,"eats bananas.")


# Create objects
lion = Lion("Simba") 
elephant = Elephant ("Dumbo") 
monkey = Monkey("George")
print(lion.make_sound()) 
print(lion.feed()) 
print("-----")
print(elephant.make_sound()) 
print(elephant.feed())
print("-----")
print(monkey.make_sound()) 
print (monkey.feed())
print("-----")