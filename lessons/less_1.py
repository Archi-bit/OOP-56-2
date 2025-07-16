
class Hero:
    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Метод класса
    def introduce(self):
        return print(f"привет меня зовут {self.name}")

# Объект/экземпляр класса
eskanor = Hero("Eskanor", 10, 40000)
naruto = Hero("Naruto", 100, 10000)


eskanor.introduce()
print(eskanor.name, eskanor.lvl, eskanor.hp)
naruto.introduce()
print(naruto.name, naruto.lvl, naruto.hp)
