from abc import ABC, abstractmethod


class Cat:
    LEG_NUM = 4

    def __init__(self, name, cat_type):
        self.name: str = name
        self.cat_type: str = cat_type

    @classmethod
    def myau(cls):
        print("Котик сделал 'Мяу'")

    @classmethod
    def leg_num(cls):
        print(f"У котенка {cls.LEG_NUM} лапы")

    @staticmethod
    def mrr():
        print("Котик сделал 'Мррр'")

    def zhrat_hochu(self):
        print(f"Котик {self.name} хочет кушать")


cat = Cat("Барсик", "Дворовой")


def sum(a, b):
    return a + b


Cat.myau()

Cat.leg_num()


cat.zhrat_hochu()


cat_2 = Cat("Мурзик", "Британец")

cat_2.zhrat_hochu()


# Инкапсуляция
# Наследование
# Полиморфизм
# Абстракция

########################################


class Dog:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if self._age < new_age:
            self._age = new_age

    def sleep(self):
        print("Свернулась калачиком и спит.")


dog = Dog("Дейзи", 7)

print(dog.age)

dog.age = 8

print(dog.age)


########################################


class HomeDog(Dog):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner


home_dog = HomeDog("Дейзи", 7, "Леха")

print(home_dog.age)
print(home_dog.name)
print(home_dog.owner)

##########################


class Parrot:

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("Залез на жердочку и уснул")


parrot = Parrot("Голубчик")

dog.sleep()
parrot.sleep()


##########################


class Animal(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @abstractmethod
    def sleep(self):
        pass


class Predator(Animal):

    def hunt(self):
        print("Охотится")


class Lion(Animal):
    def sleep(self):
        print("Zzzz....")


class Tiger(Animal):
    def sleep(self):
        print("Рычит и спит")
