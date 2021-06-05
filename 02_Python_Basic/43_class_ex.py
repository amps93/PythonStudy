class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def eat(self, food):
        print(food, '를 먹는다.')

    def sleep(self):
        print(self.name, '가 잠들다')

    def play(self):
        print(self.name, '가 놀고 있다.')

    def __str__(self):
        return self.name,self.breed,self.age,self.color

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

dog1 = Dog('a', 'Neapolitan Mastiff', 1, 'black')
dog2 = Dog('b', 'Maltese', 2, 'white')
dog3 = Dog('c', 'ChowChow', 3, 'brown')

# dog1.eat('apple')
# dog2.eat('banana')
# dog3.eat('watermelon')
# dog1.sleep()
# dog2.sleep()
# dog3.sleep()
# dog1.play()
# dog2.play()
# dog3.play()

# print(dog1.__str__())
# print(dog1.__lt__(dog2))
# print(dog1.__eq__(dog2))

if dog1 < dog2:
    print(dog2.age)
if dog2 == dog3:
    print(dog2.age,dog3.age)

# dogL = [dog1,dog2,dog3]
# for i in dogL:
#     print(dogL[i])
# print(dog1<dog2)
# print(dog1==dog3)