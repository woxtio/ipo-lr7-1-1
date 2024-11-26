import json 
with open("fishs.json", 'r', encoding='utf-8') as file: 
    data = json.load(file) 
a = 0 
while True:
    print("""
1.Вывести все записи 
2.Вывести запись по полю 
3.Добавить запись 
4.Удалить запись по полю 
5.Выйти из программы
    """)
    num = int(input("Введите номер действия: "))
    if num == 1:
        for fish in data:
            print(f"""
Номер записи: {fish['id']}, 
Общее название: {fish['name']},                       
Латинское название: {fish['latin_name']}, 
Пресноводная: {fish['is_salt_water_fish']},    
Кол-во подвидов: {fish['sub_type_count']} """)
        a += 1
    elif num == 2:
        id = int(input("Введите номер рыбы: "))
        find = False    
        for fish in data:
            if id == fish['id']:
                print(f"""
Номер записи: {fish['id']}, 
Общее название: {fish['name']},                       
Латинское название: {fish['latin_name']}, 
Пресноводная: {fish['is_salt_water_fish']},    
Количество подвидов: {fish['sub_type_count']} 
                """)
                find = True  
                break  
        a += 1
        if not find:
            print("Запись не найдена")
    elif num == 3:
        id = int(input("Введите id рыбы: "))
        exists = False
        for fish in data:
            if fish['id'] == id:
                exists = True
                break
        if exists:
            print("Такой номер уже существует")
        else:
            name = input("Введите общее название рыбы: ")  
            latin_name = input("Введите латинское название рыбы: ")  
            is_salt_water_fish = input("Является ли рыба пресноводной? (да/нет):  ")  
            sub_type_count = float(input("Введите количество подвидов: "))  
            new_fish = {
                'id': id,
                'name': name,
                'latin_name': latin_name,
                'is_salt_water_fish': True if is_salt_water_fish.lower() == 'да' else False, 
                'sub_type_count': sub_type_count
            }

            data.append(new_fish) 
            with open("fish.json", 'w', encoding='utf-8') as out_file: 
                json.dump(data, out_file)
            print("Машина успешно добавлена")
        a += 1

    elif num == 4:
        id = int(input("Введите id рыбы: "))
        find = False  

        for fish in data:
            if id == fish['id']:
                data.remove(fish)  
                find = True  
                break 

        if not find:
            print("Запись не найдена")
        else:
            with open("fish.json", 'w', encoding='utf-8') as out_file:
                json.dump(data, out_file)
            print("Запись удалена")
        a += 1
    elif num == 5:
        print(f"""Программа завершена
Количество операций: {a}""") 
        break
    else:
        print("Этот номер отсутствует")
        
