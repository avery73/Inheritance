def main():

    import Exercise as E

    name = "John"
    address = "1234 Main St"
    telephone = "123-456-7890"
    cust_num = 1234
    bool_data = False

    person1 = E.Person(name, address, telephone)
    customer1 = E.Customer(name, address, telephone, cust_num, bool_data)

    person1.print_person()
    print()
    customer1.print_person()

main()