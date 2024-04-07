import os
from PIL import Image, ImageFilter

def zd1and2():
    images1 = os.listdir() #проходимся по файлам в папке
    print(images1)
    if not os.path.isdir("zd1lab9"): #создаем папку
        os.mkdir("zd1lab9")
    for x in images1:
        if x.endswith('.jpg'): #проверяем расширение файла(зд2) и применяем фильтры
             a = Image.open(x)
             d = a.filter(ImageFilter.EDGE_ENHANCE)  # Усиление контраста на границах объектов
             a.show()
             d.show()
             d.save('zd1lab9/' + str("novo" + x))

def zd3():
    import csv
    cena = 0
    kolvo = 0
    centovara = 0
    with open('Книга1.csv',newline="") as nashcsv: #чтение
        reader = csv.DictReader(nashcsv)
        for x in reader:
            print(x)
            kolvo = int(x['Количество'])
            centovara = int(x['Цена'])
            cena +=  kolvo * centovara

    print(f"Итоговая сумма: ",cena)

zd3()