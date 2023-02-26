class Animal:
    def __init__(self, size, age, group):
        self.size = size
        self.age = age
        self.group = group

    def print_info(self):
        return f'{self.size, self.age, self.group}'


class Wolf(Animal):
    def __init__(self, name, host, sz, age, group, __eyes_color):
        super().__init__(sz, age, group)
        self.name = name
        self.host = host
        self.eyes_color = __eyes_color

    def print_info(self):
        return f'{self.name, self.host, self.size, self.age, self.group}'


class Dog(Animal):
    def __init__(self, name, color, sz, age, group):
        super().__init__(sz, age, group)
        self.name = name
        self.color = color

    def print_info(self):
        return f'{self.name, self.color, self.size, self.age, self.group}'


ob_dog = Dog('Makar', 'blue', 'big', 27, 'Staya')
ob_wolf = Wolf('Walera', 'Makar', 'small', 19, 'Svora', 'red')
ob_animal = Animal('123', 13, 'Staya')

print('-' * 50)
print('Наследование + Полиморфизм + Инкапсуляция')
print(ob_dog.print_info())
print(ob_wolf.print_info())
print(ob_animal.print_info())
print('-' * 50)
