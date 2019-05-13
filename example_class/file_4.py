class Class1:  # Базовый класс для класса Class2
    def func1(self):
        print("Метод func1() класса Class1")


class Class2(Class1):  # Класс Class2 наследует класс Class1
    def func2(self):
        print("Метод func2() класса Class2")


class Class3(Class1):  # Класс Class3 наследует класс Class1
    def func1(self):
        print("Метод func1() класса Class3")

    def func2(self):
        print("Метод func2() класса Class3")

    def func3(self):
        print("Метод func3() класса Class3")

    def func4(self):
        print("Метод func4() класса Class3")


class Class4(Class2, Class3):  # Множественное наследование
    def func4(self):
        print("Метод func4() класса Class4")


c = Class4()  # Создаем экземпляр класса Class4
c.func1()  # Выведет: Метод func1() класса Class3
c.func2()  # Выведет: Метод func2() класса Class2
c.func3()  # Выведет: Метод func3() класса Class3
c.func4()  # Выведет: Метод func4() класса Class4

# class Class4(Class2, Class3):  # Множественное наследование
#     # Наследуем func2() из класса Class3, а не из класса Class2
#     func2 = Class3.func2


print(Class1.__bases__)
print(Class2.__bases__)
print(Class3.__bases__)
print(Class4.__bases__)


class Class1:
    x = 10


class Class2(Class1):
    pass


class Class3(Class2):
    pass


class Class4(Class3):
    pass


class Class5(Class2):
    pass


class Class6(Class5):
    pass


class Class7(Class4, Class6):
    pass


c = Class7()
print(c.x)

print(Class7.__mro__)
