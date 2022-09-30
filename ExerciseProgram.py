def main():

    import Exercise as E

    name = "John"
    address = "1234 Main St"
    telephone = "123-456-7890"
    cust_num = 1234
    on_list = False # has to be uppercase False

    person1 = E.Person(name, address, telephone) # instance of superclass
    customer1 = E.Customer(name, address, telephone, cust_num, on_list) # instance of customer class

    person1.print_person()
    print()
    customer1.print_person()

main()