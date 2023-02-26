import csv


class Human(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def output(self):
        print(self.name, self.age, self.height, self.weight)


def main():
    print('Program launched')
    person1 = Human("Timur", 19, 175, 60)
    person2 = Human("Timur", 20, 170, 70)
    person1.output()
    person2.output()


if __name__ == "__main__":
    main()
