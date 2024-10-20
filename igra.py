import random


inventory = []
completed_tasks = set()


levels = {

    1: {
        'description': "Вы проснулись в разрушенном здании. Вокруг разруха и нетронутая мебель. "
                       "Вам нужно найти выход и запасы еды.",
        'task': "Найдите еду, чтобы выжить.",
        'items': ['консервы', 'бутылка воды'],
        'enemies': [],
        'next_level': 2
    },
    2: {
        'description': "Вы находитесь на улице. Слышите крики и шум. Впереди можно увидеть другую группу выживших. "
                       "Они выглядят дружелюбно, но неясно, можно ли им доверять.",
        'task': "Решите, присоединиться к ним или остаться в одиночку.",
        'items': [],
        'enemies': ['зараженный'],
        'next_level': 3
    },
    3: {
        'description': "Вы нашли укрытие в старом гараже. Нужно собрать материалы для строительства. "
                       "На земле валяются доски, гвозди и старый тент.",
        'task': "Соберите три материала для постройки убежища.",
        'items': ['доски', 'гвозди', 'тент'],
        'enemies': [],
        'next_level': 4
    },
    4: {
        'description': "Вы нашли материалы и построили убежище. Наступила ночь и Вы уснули. ",
        'task': "...",
        'items': [],
        'enemies': [],
        'next_level': 5

    },
    5: {
        'description': "Утром Вы проснулись от громкого звука.",
        'task': "Выберите, пойти на звук или остаться в убежище",
        'items': [],
        'enemies': ['толпа зараженных'],
        'next_level': None
    }
}


def show_inventory():
    if inventory:
        print("Ваш инвентарь:", ', '.join(inventory))
    else:
        print("Ваш инвентарь пуст.")


def process_command(command, current_level):
    global inventory, completed_tasks
    
    command = command.lower()
    
    if command == "осмотреться":
        print(levels[current_level]['description'])
        
    elif command == "инвентарь":
        show_inventory()

    elif command == 'задание':
        print(levels[current_level]['task'])
        
    elif command.startswith("взять "):
        item = command.split("взять ")[1]
        if item in levels[current_level]['items']:
            inventory.append(item)
            levels[current_level]['items'].remove(item)
            print(f"Вы взяли {item}.")
        else:
            print("Такого предмета здесь нет.")
            
    elif command == "присоединиться к группе":
        print("Вы присоединились к группе выживших!")
        completed_tasks.add('Присоединиться')
        return levels[current_level]['next_level']
        
    elif command == "остаться в одиночку":
        print("Вы выбрали остаться в одиночку. У вас не будет поддержки.")
        completed_tasks.add('Оставаться в одиночку')
        return levels[current_level]['next_level']
    
    elif command == "пойти на звук":
        print("Вы выбрали пойти на звук. Вы вышли из убежища и за углом Вас поджидала толпа зараженных. Вы умерли.")
        completed_tasks.add('пойти на звук')
        return None
    
    elif command == "остаться в убежище":
        print("Вы выбрали остаться в убежище. Через пару минут Вы услышали звуки пробегающей мимо толпы. Ваш выбор спас Вашу жизнь.")
        completed_tasks.add('остаться в убежище')

    elif command == "перейти на следующий уровень":
        if current_level == 1 and ('консервы' in inventory or 'бутылка воды' in inventory):
            print("Вы нашли еду и готовы покинуть разрушенное здание.")
            return levels[current_level]['next_level']
        elif current_level == 2:
            print("Вы выбрали путь выживания вместе с другими!")
            return levels[current_level]['next_level']
        elif current_level == 3 and  ('доски' and 'гвозди' and 'тент' in inventory):
            print("Вы собрали все материалы и построили новое убежище! Поздравляем!")
            return levels[current_level]['next_level']
        elif current_level == 4:
            print("Вы спокойно пережили ночь в убежище.")
            return levels[current_level]['next_level']
        elif current_level == 5:
            print("Вы выжили.")
            return levels[current_level]['next_level']
        else:
            print("Вы не выполнили условия для перехода на следующий уровень.")
            
    elif command == "выход":
        print("Вы покинули игру.")
        exit()
        
    else:
        print("Неизвестная команда.")
        
    return current_level


def main():
    current_level = 1
    while current_level is not None:
        print("\n----- Уровень", current_level, "-----")
        current_level = process_command(input("Введите команду: "), current_level)


if __name__ == "__main__":
    main()