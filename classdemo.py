



#OOP
#OBJECT ORIENTED PROGRAMMING

class Adventurer():
    # what is in their pockets?
    # what is their health?
    # how hard can they attack?

    def __init__(self):
        self.inventory = ["candle", "book of matches"]
        self.health = 10
        self.strength = 6

    def potion(self):
        self.health += 5

    def punch(self, other_adventureer: Adventurer):
        other_adventurer.health -= self.strength

captain_lb = Adventurer()
general_zo = Adventurer()

general_zo.punch(captain_zo)


print(dir(captain_lb))
print(captian_lb.health)
print(general_zo.health)

general_zo.potion()


