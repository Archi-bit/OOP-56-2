# # Наследование
#
# # Родительский|Супер класс
# class Hero:
#
#     def __init__(self, name, lvl, age, hp):
#         self.name = name
#         self.lvl = lvl
#         self.age = age
#         self.hp = hp
#
#     def action(self):
#         return print(f"Base action")
#
# # Дочерний класс
# class Magic(Hero):
#
#     def __init__(self, name, lvl, age, hp, mp):
#         super().__init__(name, lvl, age, hp)
#         self.mp = mp
#
#
#     def rest(self):
#         return print (f"Я отдыхаю")
#
#     def action(self):
#         return print(f"========")
#
#
# hero = Magic("Atractor", 100, 32, 1000, 500)
#
# hero.action()



class Animal:
    def action(self):
        return print(f"Animal")

class Swim(Animal):
    def action(self):
        return print(f"Swimmer")
class Fly(Animal):
    def action(self):
        return print(f"Fly")
class Duck(Fly, Swim):
    pass

donald_trampaduck = Duck()
print(Duck.mro())
# donald_trampaduck.action()