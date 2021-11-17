def man():
    d_1 = "\n Enter 1 - to see list of all workers\n"
    d_2 = "Enter 2 - to see 'to-do list'\n"
    d_3 = "Enter 3 - list of instructions to employees\n"
    d_4 = "Enter 4 - show a list of all coverage for specific areas\n"
    d_5 = "Enter 5 - show the amount for real estate, for sale, for rent\n"
    d_6 = "Enter 6 - calculate% by category of real estate\n"
    print(d_1,d_2,d_3,d_4,d_5,d_6)
    m=int(input("Please dial the menu number to work with the program,\n If you're done, dial 7:"))
    return m
