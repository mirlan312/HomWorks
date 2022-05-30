GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bug': {'fails', 'errors', 'stack'}
}
del GeekTech["bug"]
GeekTech["address"] = "Ibraimova, 103 Bishkek, 720011"
courses = dict()
courses["courses"] = "UX/UI Disaner", "FusllStack", "IOS"
GeekTech.update(courses)
GeekTech["phone"] = +996507052018, +996777052018, +996557052018,
GeekTech["instagram"] = "geektech__kg",


for key, value in GeekTech.items():
    print(f'{key}: {value}')

print(GeekTech)