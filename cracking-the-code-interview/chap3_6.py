import unittest
import time


class Animal():
    def __init__(self, name):
        self.name = name
        self.timeStamp = time.time()
        st = input(">>")

    def __str__(self):
        return self.name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalShelter():
    def __init__(self):
        self.dog = []
        self.cat = []

    def enqueue(self, animal):
        if animal.__class__ == Dog:
            self.dog.append(animal)
        else:
            self.cat.append(animal)

    def dequeueDog(self):
        if len(self.dog) == 0:
            return None
        dog = self.dog[0]
        self.dog = self.dog[1:]
        return dog

    def dequeueCat(self):
        if len(self.cat) == 0:
            return None
        cat = self.cat[0]
        self.cat = self.cat[1:]
        return cat

    def dequeueAny(self):
        if len(self.cat) == 0:
            return self.dequeueDog()
        elif len(self.dog) == 0:
            return self.dequeueCat()

        if self.cat[0].timeStamp < self.dog[0].timeStamp:
            return self.dequeueCat()

        else:
            return self.dequeueDog()


class Test(unittest.TestCase):
    def test_animal_shelter(self):
        shelter = AnimalShelter()
        shelter.enqueue(Cat("Hanzack"))
        shelter.enqueue(Dog("Pluto"))
        shelter.enqueue(Cat("Garfield"))
        shelter.enqueue(Cat("Tony"))
        shelter.enqueue(Dog("Clifford"))
        shelter.enqueue(Dog("Blue"))
        self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
        self.assertEqual(str(shelter.dequeueAny()), "Pluto")
        self.assertEqual(str(shelter.dequeueDog()), "Clifford")
        self.assertEqual(str(shelter.dequeueDog()), "Blue")
        self.assertEqual(str(shelter.dequeueCat()), "Garfield")
        self.assertEqual(str(shelter.dequeueCat()), "Tony")
        self.assertEqual(str(shelter.dequeueAny()), "None")
        self.assertEqual(str(shelter.dequeueAny()), "None")


if __name__ == "__main__":
    unittest.main()
