import random
def zd12():
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан:{self.restaurant_name},Кухня:{self.cuisine_type}")

        def open_restaurant(self):
            op = random.randint(0, 1)
            if op == 1:
                return "Ресторан открыт!"
            else:
                return "Ресторан закрыт."


    print("Задание 1")
# создаем экземпляр класса и выводим
    NewRestaurant = Restaurant('Плаз', 'Итальянская')
    print(f"Название ресторана: {NewRestaurant.restaurant_name}")
    print(f"Кухня ресторана: {NewRestaurant.cuisine_type}")
    print(NewRestaurant.describe_restaurant(), NewRestaurant.open_restaurant())

    print("Задание 2")
    rest1 = Restaurant("Дум", 'Греческая')
    rest2 = Restaurant('Орез', 'Немецкая')
    rest3 = Restaurant('Ямб', 'Русская')

    rest1.describe_restaurant()
    rest2.describe_restaurant()
    rest3.describe_restaurant()

def zd3():
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан:{self.restaurant_name},Кухня:{self.cuisine_type},Рейтинг:{self.rating}")

        def changerating(self, newrating):
            self.rating = newrating

    rest1 = Restaurant("Дум", 'Греческая', 0)
    rest2 = Restaurant('Орез', 'Немецкая', 0)
    rest3 = Restaurant('Ямб', 'Русская', 0)
    print(f"Изначальный рейтинг ресторана Дум: {rest1.rating}")
    print(f"Изначальный рейтинг ресторана Орез: {rest2.rating}")
    print(f"Изначальный рейтинг ресторана Ямб: {rest3.rating}")
    smena = input("Хотели бы вы поменять рейтинг у ресторана?(+/-): ")
    if smena == "+":
       print("У какого ресторана Вы бы хотели поменять рейтинг?")
       print("1-Дум")
       print("2-Орез")
       print("3-Ямб")
    v = int(input("Ваш ответ: "))
    newrating = input("Ваша оценка: ")
    if v == 1:
        rest1.changerating(newrating)
        rest1.describe_restaurant()
    elif v == 2:
        rest2.changerating(newrating)
        rest2.describe_restaurant()
    else:
        rest3.changerating(newrating)
        rest3.describe_restaurant()

#12 ЛАБОРАТОРНАЯ
def zd1lab12():
    class Restaurant():
        def __init__(self,restaurant_name,cuisine_type):
            self.restaurant_name =restaurant_name         #input(restaurant_name)
            self.cuisine_type = cuisine_type            #input(cuisine_type)
        def describe_restaurant(self):
            print(f"Ресторан:{self.restaurant_name},Кухня:{self.cuisine_type}")

        def open_restaurant(self):
                op = random.randint(0, 1)
                if op == 1:
                    return "Ресторан открыт!"
                else:
                    return "Ресторан закрыт."

    NewRestaurant = Restaurant('Плаз', 'Итальянская')
    print(f"Название ресторана: {NewRestaurant.restaurant_name}")
    print(f"Кухня ресторана: {NewRestaurant.cuisine_type}")
    print(NewRestaurant.describe_restaurant(), NewRestaurant.open_restaurant())
    #x1 = Restaurant("Название ресторана: ", "Кухня: ") - для вводимого
    #print(x1.describe_restaurant(), x1.open_restaurant()) -для вводимого
    class IceCreamStand(Restaurant):
        flavors = ['клубничное', 'ванильное', 'фисташковое']
        typesicecream = ['на палочке','в рожке','мягкое мороженое','лёд']
        def __init__(self, restaurant_name, cuisine_type, location, working_hours):
            super().__init__(restaurant_name, cuisine_type)
            self.location = location
            self.working_hours = working_hours
        def describe_cafe1(self):
            print(f"Дополнительно:{self.restaurant_name},Кухня:{self.cuisine_type}")
        def describe_cafe(self):
            print(f"Локация кафе:{self.location},Часы работы:{self.working_hours}")

        def display_flavors(self): #метод,который выводит список сортов мороженого
            print("Список доступных вкусов мороженого:")
            for flavor in self.flavors:
                print(flavor)
        def display_typesicecream(self): #метод,который выводит список типов мороженого
            print("Список доступных типов мороженого:")
            for type in self.typesicecream:
                print(type)
        def typemotion(self): #метод для работы с выбранным типом мороженого
            print(f'Вы выбрали тип: {type1}')
            if type1 in self.typesicecream:
                print('Тип мороженого в наличии')
            else:
                print('Такого мороженого нет')
        def add_type(self):
                if b == '+':
                    type2= input('Добавляем тип: ')
                    print(f'Выбранные типы мороженого: {type1},{type2}')

#метод добавление сорта мороженого
        def add_flavor(self, flavor):
                self.flavors.append(flavor)
#метод удаление сорта мороженого
        def remove_flavor(self, flavor):
                if flavor1 in self.flavors:
                    self.flavors.remove(flavor1)
                    print(f"Мороженое вкуса {flavor1} удалено.")
                else:
                    print(f"{flavor1} -такого мороженого нет в списке.")
#метод проверки наличия вкуса
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                    print(f"Да, {flavor} мороженое есть.")
            else:
                    print(f"К сожалению вкуса {flavor} нет в наличии.")
    # Создание экземпляра класса IceCreamStand и вывод
    ice_cream_stand = IceCreamStand("Кафе-мороженое", "холодные десерты","Наб.Обводного канала,дом 100","10-22:00")
    ice_cream_stand.describe_cafe1()
    ice_cream_stand.display_flavors() #вызов метода
    ice_cream_stand.describe_cafe()
    flavor = input("Введите сорт мороженого для добавления: ")
    ice_cream_stand.add_flavor(flavor)
    print("Обновленный список сортов: ")
    ice_cream_stand.display_flavors()
    flavor_to_check = input("Введите сорт мороженого для проверки: ")
    ice_cream_stand.check_flavor(flavor_to_check)
    flavor1 = input("Введите сорт мороженого для его удаления: ")
    ice_cream_stand.remove_flavor(flavor1)
    ice_cream_stand.display_flavors()
    ice_cream_stand.display_typesicecream()
    type1 = input("Какой тип мороженого вы бы хотели?: ")
    ice_cream_stand.typemotion()
    print('Добавить в список ваших типов мороженого еще один?')
    b = input('+/-')
    ice_cream_stand.add_type()

zd1lab12()