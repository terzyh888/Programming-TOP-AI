class SpaceShip:  # Имеет атрибуты для управления топливом, состоянием корпуса, и текущей скоростью.
    def __init__(self, fuel, hull_condition, speed):
        self.fuel = fuel  # топливо
        self.hull_condition = hull_condition  # состояние корпуса
        self.speed = speed  # текущая скорость


class CrewMember:  # Контролирует здоровье, навыки, и роли в команде (например, пилот, инженер).
    def __init__(self, name, health, skills, role):
        self.name = name
        self.health = health  # здоровье
        self.skills = skills  # навыки
        self.role = role  # роль (например, пилот)


class Mission:  # Определяет цели, ресурсы, и возможные события (например, аварии, встречи с астероидами).
    def __init__(self, objectives, resources, events):
        self.objectives = objectives  # цели
        self.resources = resources  # ресурсы
        self.events = events  # возможные события (аварии, астероиды)

    def start_mission(self, ship):
        print(f"Миссия началась! Цель: {self.objectives}")
        print(f"Случившееся событие: {self.events}")

        # Простейшее изменение параметров корабля при событии
        if "астероид" in self.events.lower():
            ship.hull_condition -= 20
            print("Корабль столкнулся с астероидом! Корпус поврежден.")
        elif "авария" in self.events.lower():
            ship.fuel -= 30
            print("Произошла авария! Потрачено много топлива.")


# Проверка работы:
my_ship = SpaceShip(fuel=100, hull_condition=100, speed=5000)
pilot = CrewMember(name="Иван", health=100, skills=["пилотирование"], role="Пилот")

space_mission = Mission(
    objectives="Добраться до Марса",
    resources=["вода", "еда"],
    events="Встреча с астероидами"
)

space_mission.start_mission(my_ship)
print(f"Остаток топлива: {my_ship.fuel}")
print(f"Состояние корпуса: {my_ship.hull_condition}")