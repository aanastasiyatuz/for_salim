def m_2():
    import m
    bg=840
    prom=input(" \nFacebook \nInstagram \nGoogle Ads \nYouTube \nChoose a title to promote:")
    if prom=="Facebook":
        am=int(input("Type the amount of expense you want to spend from the budget:"))
        if am>bg:
            print("amount exceeded!")
            m_2()
        if am<bg:
            print(" Sucsess!\n You have",bg-am,"$ left")
            m.m()
    if prom=="Instagram":
        am=int(input("Type the amount of expense you want to spend from the budget:"))
        if am>bg:
            print("amount exceeded!")
            m_2()
        if am<bg:
            print(" Sucsess!\n You have",bg-am,"$ left")
            m.m()
    if prom=="Google Ads":
        am=int(input("Type the amount of expense you want to spend from the budget:"))
        if am>bg:
            print("amount exceeded!")
            m_2()
        if am<bg:
            print("You have",bg-am,"$ left")
            m.m()
    if prom=="YouTube":
        am=int(input("Type the amount of expense you want to spend from the budget:"))
        if am>bg:
            print("amount exceeded!")
            m_2()
        if am<bg:
            print(" Sucsess!\n You have",bg-am,"$ left")
            m.m()
