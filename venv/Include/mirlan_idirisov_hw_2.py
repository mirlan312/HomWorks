while True:
    text = input('пишите слова: стоп если хотете остановить')
    if text == "стоп":
        break
    string = text.lower()
    count = 0
    list1 = "ауоыиэяеaeiouАОЫИЭЯЕEAEIOU"
    for i in text:
        if i in list1:
            count = count + 1
    count1 = 0
    list2 = "бвгджзйклмнпрстфччшщbcdfghjklmnpqrstvwxyzБВГДЖЭЙКЛМНПРСТФХЦЧШЩBCDFGHJKLMNPRSTVWYZ"
    for i in text:
        if i in list2:
            count1 = count1 + 1

    count3 = 0
    for i in text:
        if i in list1 or list2:
            count3 = count3 + 1

    print(f"Слово: {text}")
    print(f"количество букв: {count3}")
    print(f"гласные буквы: {count}")
    print(f"согласные буквы: {count1}")
    print(f'Гласные: {round(count / len(text) * 100,2)}%'"/"f'Согласные: {round(count1 / len(text) * 100,2)}%')