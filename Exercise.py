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
    def __init__(self, name, address, telephone, cust_num, bool_data):
        Person.__init__(self, name, address, telephone)
        self.__cust_num = cust_num
        self.__bool_data = bool_data
            # can't print attributes in subclass

    def get_cust_num(self):
        return self.__cust_num
    
    def get_bool_data(self):
        return self.__bool_data

    def print_person(self):
        print("Method 1")
        print("Name:", Person.get_name(self))

        #OR
    print()

    #print("Method 2")
    #Person.print_person(self)

    print("Customer Number:", self.__cust_number)
    if self.__bool_data:
        print("On Mailing List")
    else:
        print("Not on Mailing List")