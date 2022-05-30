class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married


introduce_myself = Person(fullname="Azamat", age=24)
print(introduce_myself)
print(f"{introduce_myself.fullname} {introduce_myself.age}")
