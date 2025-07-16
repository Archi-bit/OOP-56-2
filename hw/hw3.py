# Дз 3.1

# class Student:
#     def __init__(self, name, grade, password):
#         self.name = name
#         self._grade = grade
#         self.__password = password
#
#     def change_password(self, new_pass):
#         self.__password = new_pass
#         print("Пароль успешно изменен")
#
#     def get_info(self):
#         print(f"Имя: {self.name}, Оценка: {self._grade}")
# # пример использования
#
# student = Student("Aizat", 95, 4587)
# student.get_info()
# student.change_password("new_secure_password")


# Дз 3.2

# from abc import ABC, abstractmethod
#
# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def move(self):
#         print("Машина едет")
#
#     def stop(self):
#         print("Машина остановилась")
#
# class Bike(Vehicle):
#     def move(self):
#         print("Велосипед едет")
#
#     def stop(self):
#         print("Велосипед остановился")


# пример использования

# car = Car()
# bike = Bike()
#
# car.move()
# car.stop()
#
# bike.move()
# bike.stop()
