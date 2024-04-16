#10 лабораторная
def zd1lab10():
    import json
    #считываем информацию с файла
    with open('doc.json', 'r',encoding="utf-8") as chit:
      chtenie = json.load(chit)
    # проходимся по каждому продукту и выводим информацию
    for x in chtenie['products']:
      print(f"Название: {x['name']}") #выводим значения ключей(тут name-это ключ,знач-е кот.выводим)
      print(f"Цена: {x['price']}")
      print(f"Вес: {x['weight']}")
      if x['available'] == True:
        print("В наличии")
      else:
        print("Нет товара в наличии...")
    print()
def zd2lab10():
    import json
    # считываем информацию с файла
    with open('docdop.json', 'r', encoding="utf-8") as chit:
        chtenie = json.load(chit)
        new = {
            "name": input("Введите новый товар: "),
            "price": int(input("Введите цену товара: ")),
            'available': input("Товар есть в наличии?(True/False): ").lower() == "true",  # .lower() == "true",
            "weight": int(input("Введите вес товара: "))
        }
        chtenie['products'].append(new)
        with open('docdop.json', 'w', encoding="utf-8") as f:
            json.dump(chtenie, f)
            print("Содержимое файла после добавления продуктов:")
        for x in chtenie['products']:
                print(f"Название: {x['name']}")  # выводим значения ключей(тут name-это ключ,знач-е кот.выводим)
                print(f"Цена: {x['price']}")
                print(f"Вес: {x['weight']}")
                if x['available'] == True:
                    print("В наличии")
                else:
                    print("Нет товара в наличии...")
    print()
def zd3lab10():
# считываем данные из файла en-ru.txt и из текстового файла делаем словарь
    with open('en-ru.txt','r',encoding = 'utf-8') as nashtxt:
        anglrusslov = {}
        chitaemstroki = nashtxt.readlines()
        # обработка данных и заполнение словаря
        for line in chitaemstroki: #проходимся по строкам из прочитанного
          chast = line.strip().split(' - ') #strip убирает пробелы по бокам слова\строки
          #разделяем знаком "-",именно так разбивается на части
          engslovo = chast[0] #при делении сплитом строка разбивается на подстроки по индексам
          if len(chast) > 1: #если слов в строке больше единицы(то есть англ слово+перевод)
              russslova = chast[1].split(', ') #делим запятыми если слов несколько
              anglrusslov[engslovo] = russslova #проходится по англ.словам и дает им перевод
#создаем русско-английский словарь
    rusanglslov = {}
    for line in chitaemstroki:
        en, ru = line.strip().split(' - ')
        russkiewords = ru.split(', ')
        for rusword in russkiewords:
            if rusword in rusanglslov: #слово зачислено в словарь-ставим к нему английское
                rusanglslov[rusword].append(en)
            else:
                rusanglslov[rusword] = [en]
#создаем текстовый ru-en.txt и записываем в него все
    with open('ru-en.txt', 'w', encoding='utf-8') as novirustxt:
        sortirovka = sorted(rusanglslov.keys())
        for rusword in sortirovka:
            engwords = ', '.join(rusanglslov[rusword])
            novirustxt.write(f'{rusword} - {engwords}\n')
zd3lab10()
