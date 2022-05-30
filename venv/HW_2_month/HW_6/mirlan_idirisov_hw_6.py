import re


class data:
    def __init__(self, full_name, email, file_name, color):
        self.full_name = full_name
        self.email = email
        self.file_name = file_name
        self.color = color

        @property
        def full_name(self):
            return self.full_name

        @full_name.setter
        def full_name(self, value):
            self.full_name = value

        @property
        def email(self):
            return self.email

        @email.setter
        def email(self, value):
            self.email = value

        @property
        def file_name(self):
            return self.file_name

        @file_name.setter
        def file_name(self, value):
            self.file_name = value

        @property
        def color(self):
            return self.color

        @color.setter
        def color(self, value):
            self.color = value

files = ['full_name.txt', 'email.txt', 'file_name.txt', 'color.txt']


with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
    for i in file:
        content = file.read()

        full_name_list = re.findall(r'[A-Z]+[a-z]+.\D.[A-Z]+[a-z]+', content)
        print(full_name_list)

        email_list = re.findall(r'\w+@\w+\.\w+', content)
        print(email_list)

        color_list = re.findall(r'#......', content,)
        print(color_list)


        with open(files[0], 'a') as fullN:
            fullN.write(str(full_name_list))
            fullN.write('\r')
        with open(files[1], 'a') as emailN:
            emailN.write(str(email_list))
            emailN.write('\r')
        # with open(files[2], 'a') as fileN:
        #     fileN.write(info.file_name)
        #     fileN.write('\r')
        with open(files[3], 'a') as colorN:
            colorN.write(str(color_list))
            colorN.write('\r')

def RemList():
    file = open('full_name_list.txt', 'w')
    file.close()

    file = open('email_list.txt', 'w')
    file.close()

    file = open('file_name_list.txt', 'w')
    file.close()

    file = open('color_list.txt', 'w')
    file.close()

RemList()
