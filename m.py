def m():
    d_1 = "\n Enter 1 - to see list of places for marketing\n"
    d_2 = "Enter 2 - to see list of areas for marketing\n"
    d_3 = "Enter 3 - to see total budget for marketing\n"
    d_4 = "Enter 4 - to spend budget on promotion\n"
    print(d_1,d_2,d_3,d_4)
    i=int(input("Please dial the menu number to work with the program,\n If you're done, dial 5:"))
    if i==1:
        print("\nFacebook - 2.8 billion users \nInsagram - 500 million users \nGoogle Ads - 3.5 billion users \nYouTube - 2.3 billion users")
        m()
    elif i==2:
        budg=int(input("\n1 - Facebook \n2 - Instagram \n3 - Google Ads \n4 - YouTube \nSelect one from the list:"))
        if budg==1:
            print('it will cost $1,72 for one click, or \n399 $ - Facebook ad impressions up to 400 thousand \n$ 599 - Facebook ad impressions up to 600 thousand \n$ 799 - Facebook ad impressions up to 800 thousand \n$ 999 - Facebook ad impressions up to 1 million')
            m()
        if budg==2:
            print('1$ for 1 day,or \n150$ for 30 day')
            m()
        if budg==3:
            print('4,26$ for 30 day, \ntotal budget - 129.64$')
            m()
        if budg==4:
            print('0.85$ per 1000 views')
            m()
    elif i==3:
        budg=("total budget for marketing: 638,26$ for month")
        print(budg)
        m()
    elif i==4:
        import m_2
        m_2.m_2()
                
    elif i==5:
        print("the program is over, we look forward to your return! ")
    elif i<1 or i>5:
        print("Error. Try it again")
        m()
