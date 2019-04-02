

def write():

    print("For how many days do you have sales?")
    sale_days = input()
    sale_days = int(sale_days)

    file_writing = open('sales.txt','w')

    for daysale in range(1, sale_days+1,):
        print("Enter the sales of the day #",daysale)
        daysale = input()
        file_writing.write(daysale+'''
''')




    file_writing.close()






write()