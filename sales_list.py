

def sales():
    list_sales = []
    days = 1
    index = 0

    print("Enter the sales for each day")
    while days < 6:
        print("ENTER THE SALE FOR DAY #",days)
        amount = input()
        list_sales.insert(index,amount)
        days = days+1
        index = index +1


    print("The sales you have entered: ")


    for x in range(len(list_sales)):
        print (list_sales[x])




sales()