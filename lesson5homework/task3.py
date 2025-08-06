from abc import ABC, abstractmethod
from enum import Enum
import random


class CharacterClass(Enum):
    WARRIOR = "Воин"
    ARCHER = "Лучник"
    MAGE = "Маг"


class Equipment:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def equip(self, character):
        pass

    @abstractmethod
    def unequip(self, character):
        pass

    @abstractmethod
    def get_equipment_type(self):
        pass


class Weapon(Equipment):
    def __init__(self, name, base_attack=20):
        super().__init__(name)
        self.base_attack = base_attack

    def equip(self, character):
        character.base_attack += self.base_attack
        return (
            f"Оружие '{self.name}' экипировано. Атака увеличена на {self.base_attack}"
        )

    def unequip(self, character):
        character.base_attack -= self.base_attack
        return f"Оружие '{self.name}' снято. Атака уменьшена на {self.base_attack}"

    def get_equipment_type(self):
        return "Оружие"


class Armor(Equipment):
    def __init__(self, name, max_health=100):
        super().__init__(name)
        self.max_health = max_health

    def equip(self, character):
        character.max_health += self.max_health
        return (
            f"Броня '{self.name}' экипирована. Здоровье увеличено на {self.max_health}"
        )

    def unequip(self, character):
        character.max_health -= self.max_health
        return f"Броня '{self.name}' снята. Здоровье уменьшено на {self.max_health}"

    def get_equipment_type(self):
        return "Броня"


class Accessory(Equipment):
    def __init__(self, name, max_mana=30):
        super().__init__(name)
        self.max_mana = max_mana

    def equip(self, character):
        character.max_mana += self.max_mana
        return f"Аксессуар '{self.name}' экипирован. Запас маны увеличен на {self.max_mana}"

    def unequip(self, character):
        character.max_mana -= self.max_mana
        return f"Аксессуар '{self.name}' снят. Запас маны уменьшен на {self.max_mana}"

    def get_equipment_type(self):
        return "Аксессуар"


class Character(ABC):
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        self.max_health = 100
        self.current_health = self.max_health
        self.max_mana = 50
        self.current_mana = self.max_mana
        self.base_attack = 20
        self.critical_attack = 120
        self.equipment = {}
        self.active_effects = []

    @abstractmethod
    def special_ability(self, target):
        pass

    def attack(self, target):
        print(f"Атакует {target}")

    def take_damage(self, damage):
        print(f"Получает урон в размере {damage} единиц")

    def level_up(self):
        print("Уровень повышен!")

    def is_alive(self):
        print("Ты всё ёщё жив!")


class Warrior(Character):
    def __init__(self, name, character_class):
        super().__init__(name, character_class)
        self.counter_for_special = 3
        self.max_health = 200
        self.base_attack = 20

    def special_ability(self):
        print("Переход в режим ярости")
        if self.counter_for_special > 0:
            self.base_attack *= 2
            self.counter_for_special -= 1
            return f"Режима ярости хватит ещё на {self.counter_for_special} хода"
        else:
            self.counter_for_special = 3
            return "Перезарядка"

    def take_damage(self, damage):
        a = random(1, 5)
        if a == 5:
            return "Урон был заблокирован"
        else:
            return super().take_damage(damage)


class Archer(Character):
    def __init__(self, name, character_class):
        super().__init__(name, character_class)
        self.max_health = 100
        self.base_attack = 40

    def accurate_shot(self, target):
        print(
            f"{target} получает критический урон: {self.critical_attack} единиц урона"
        )

    def take_damage(self, damage):
        b = random(1, 10)
        if b in [1, 2, 3]:
            return "Перекат"
        else:
            return super().take_damage(damage)


class Mage(Character):
    def __init__(self, name, character_class):
        super().__init__(name, character_class)
        self.max_health = 50
        self.base_attack = 10
        self.fireball_attack = 30

    def fireball(self, targets):
        self.current_mana -= 30
        print(
            f"{targets} были атакованы огненным шаром и получили {self.fireball_attack} единиц урона"
        )

    def mana_recovery(self):
        if self.current_mana < self.max_mana:
            self.current_mana += 10
            return f"У вас есть {self.current_mana} единиц маны"
        else:
            return "Мана полностью восстановлена"
