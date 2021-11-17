import account
print("Estate agency 'SAB' is greeting you!")

def menu():
    account.main()
    a=input('To run the program, please enter your account type:')
    if a=='marketing':
        import m
        b=input("Enter password:")
        if b=='marketing':
            print("Greetings dear Marketer!")
            m.m()
        else:
            print("Sorry, please try again.")
            menu()
    elif a=='director':
        b=input("Enter password:")
        if b=='director':
            print("Greetings dear Director!")
            d()
        else:
            print("Sorry, please try again.")
            menu()
    elif a=='sale-manager':
        b=input("Enter password:")
        if b=='sale-manager':
            print("Greetings dear Sale-manager!")
            s()
        else:
            print("Sorry, please try again.")
            menu()
    elif a=='manager':
        b=input("Enter password:")
        if b=='manager':
            import man
            print("Greetings dear Manager!")
            man.man()
        else:
            print("Sorry, please try again.")
            menu()
    elif a=='worker':
        b=input("Enter password:")
        if b=='worker':
            import w
            print("Greetings dear Worker!")
            w.w()
        else:
            print("Sorry, please try again.")
            menu()
    else:
        print('Sorry, but we did not find this type of account, please repeat.')
        menu()


menu()
