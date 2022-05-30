class Computer:
    
    def __init__(self, cpu, memery):
        self.__cpu = cpu
        self.__memery = memery

    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memery(self, value):
        self.value = value

    @memery.setter
    def memery(self, value):
        self.value = value

    def str(self, cpu, memory):
        return f"Cpu: {cpu}, memory: {memory}"

    def gt(self, other):
        return self.memery > other.memory

    def ge(self, other):
        return self.memery >= other.memory

    def eg(self, other):
        return self.memery == other.memory


    def make_computations(self):
        self.cpu = value
        self.__memery = value
        print(self.__cpu >= self.__memory)
        print(self.__cpu > self.__memory)
        print(self.__memory - self.__cpu)


class Phone:

    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_cards_list, call_to_number):
        self.__call_to_number = call_to_number
        self.__sim_cards_list = sim_cards_list
        while True:
            sim_cards_list = int(input("Enter sim card"))
            if sim_cards_list == 1:
                print(f"You have chosen a sim card {sim_cards_list}")
                call_to_number = int(input("Enter phone number:"))
                if call_to_number == str:
                    print("Phone number can only be numeric!")
                continue
                print(f"You are call to number: {call_to_number}, in sib card: {sim_cards_list}")
            elif sim_cards_list > 1:
                print("You got just 1 sim card!")
                continue
            else:
                print('You have entered incorrect characters!')

            def __str(sefl):
                super(Phone, self).__str(f'Sim_card: {sim_cards_list}')
                

class SmarthPhone(Computer,Phone):
    def __init__(self, cpu, memory, location):
        self.cpu = cpu
        self.memory = memory
        self.location = location

    def use_gps(self, location):
        self.location = location
        while True:
            print('GPS on')
            location = input('Where do you want to route?:')
            if len(location) > 50:
                print("Maximum input characters 50!")
                continue
            elif len(location) < 3:
                print("Minimum character input 3!")
                continue
            elif location == 'quit':
                print("You have completed the GPS program.")
                break
            else:
                print(f'You have routed to {location}.')

    def str(self):
        return super(SmartPhone, self).str(f"Location: {self.location}") + f"Cpu: {self.cpu}, " \
                                                                           f"Memory: {self.memory}" \
                                                                           f"Sim_card: {self.sim_cards_list}"

    my_comp = Computer(4, 8096)
    my_phone = Phone("O!")
    my_smartphone = SmarthPhone("Bishkek", 8, 4096)
    my_smartphone2 = SmarthPhone("Tash DOBO", 7, 3072)
    # my_smartphone.use_gps("Bishkek")
    # my_phone.call("MegaCom", 0)
    my_comp.make_comulations(4)
