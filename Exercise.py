class Person:
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone
    
    def print_person(self):
        print("Name:", self.__name)
        print("Address:", self.__address)
        print("Telephone:", self.__telephone)

class Customer(Person):
    def __init__(self, name, address, telephone, cust_num, on_list):
        Person.__init__(self, name, address, telephone)
        self.__cust_num = cust_num
        self.__on_list = on_list
            # can't print attributes in subclass

    def print_person(self):
        print("Method 1")
        print("Name:", Person.get_name(self)) # called from superclass
        print("Address:", Person.get_address(self))
        print("Phone:", Person.get_telephone(self))

    #OR
        print()

        print("Method 2")
        Person.print_person(self) # could call print person method of superclass

        print("Customer Number:",self.__cust_num)
        if self.__on_list:   # means if on_list == True:
            print("On Mailing List")
        else:
            print("Not on Mailing List")