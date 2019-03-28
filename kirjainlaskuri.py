

def main():
    counter = 0
    string1 = input("enter a sentence")
    for ch in string1:
        if ch == 'T' or ch== 't':
            counter += 1

    print("T-kirjaimia yhteensä:",counter)


main()