mentors = ['Эсенбек', 'Мирхад', 'Беки']
while True:
    menu = input(' \n 1-Добавление : \n 2-Изменение : \n 3-Удаление : \n 0-Выход : \n')
    if menu == '1':
        print('Добавление:')
        name = input('name').capitalize()
        if len(mentors) <= 4:
            if len(name) >= 15:
                print('Слишком много букв!')
            else:
                mentors.append(name)
                print(mentors)
        else:
            print('Слишком много ментаров!')
    elif menu == '2':
        print('Изменение:')
        if menu == '2':
            zamena = input('Введите имя, которую хотите заменить:').capitalize()
            new = input('Новое имя:').capitalize()
            if zamena in mentors and len(new) <= 15:
                mentors.remove(zamena)
                mentors.append(new)
            elif zamena in mentors and len(new) != 15:
                print('Имя больше 15 букв!')
            else:
                print('Такого ментора нет!')
    elif menu == '3':
        print('Удаление:')
        if menu == '3':
            delete = input('Введите имя или индекс')
            if delete == 'индекс':
                delete = int(input('индекс'))
                if delete > len(mentors) - 1:
                    print('Такого индекса нет!')
                    continue
                else:
                    del mentors[delete]
            elif delete == 'name':
                name1 = input('name:')
                if name1 in mentors:
                    mentors.remove(name1)
                    print(mentors)
                else:
                    print('Такого ментора нет!')
            else:
                print('Такой команды нет!')
                continue
    elif menu == '0':
        list = tuple(mentors)
        print(list)
        break
    else:
        print('Есть команды: 1, 2, 3, 0!')