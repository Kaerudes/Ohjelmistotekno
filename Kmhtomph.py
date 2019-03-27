def Kmh_to_mph():

    print("KPH          MPH")
    print("-----------------")
    kph = 60
    for kmh in range (60,131,10):
        mph = kmh*0.62137
        print(kmh, "          ",format(mph,".2f"))




Kmh_to_mph()