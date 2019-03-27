def retail_price_input():

    print("Enter the items wholesale cost:")
    cost = float(input())
    while cost < 0:
        print("Error price can't be negative")
        print("Enter the correct wholesale price:")
        cost = float(input())
    retailprice = cost ** 2.5
    retailprice = str(retailprice)
    print("Retail price:" + retailprice)
    print("Do you have another product? (y/n)")
    yesno = input()
    if yesno == "y" or "Y":
       return  retail_price_input()



retail_price_input()

