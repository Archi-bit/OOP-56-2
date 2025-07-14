class Robot:
    def __init__(self, model, speed, battery_life):
        self.model = model
        self.speed = speed
        self.battery_life = battery_life

    def info(self):
        return f"Модель: {self.model}, Скорость: {self.speed} км/ч, Время работы: {self.battery_life} часов"

    def distance(self):
        return self.speed * self.battery_life


robot1 = Robot("RX-78", 15, 8)
robot2 = Robot("T-800", 20, 5)

print(robot1.info())
print(f"Максимальное расстояние: {robot1.distance()} км\n")

print(robot2.info())
print(f"Максимальное расстояние: {robot2.distance()} км")
