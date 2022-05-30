ten = [i for i in range(1,11)]
evens = list(filter(lambda x: x % 2 == 0, ten))
up = list(map(lambda x: x**2, evens))

print(f'Сгенерированный список ten от 1 до 10: {ten}')
print(f'Четные числа из списка ten {evens}')
print(f'Возведенные в квадрат числа из списка evens {up}')

def show_Idx(lst= ten):
    try:
        print(lst)
        Idx = int(input('Введите индекс объекта из списка который хотите вывести: '))
        if Idx > 0 and Idx <= len(lst) - 1:
            print(f'Под индексом: {Idx} находится объект: {lst[Idx]}')
        else:
            print(f"Пишите индекс только от 0 до {len(lst) - 1}")
    except Exception:
        print("Введите только  числа!")


while 1:
    comand = input('Выбери действия: \n1)Вывести элемент по индексу\n0)Выход\n')
    if comand == '1':
        show_Idx()
    elif comand == '0':
        print("Program finished")
        break
    else:
        print('Нет такой меню пишите только числа 1 или 0!')
        continue