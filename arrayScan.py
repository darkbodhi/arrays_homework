def arrayScan():

    myarray = []
    quantity = int(input("Please, insert the number of symbols to be scanned: "))
    symb_input = str(input("Please, insert the symbols to add to an array:"))
    if len(symb_input) == quantity:
        print("The execution of program is succesful.")
    else:
        raise Exception("An error has occurred.")