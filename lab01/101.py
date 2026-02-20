def val(number):
    while number>0:
        a=number%10
        if a%2==0:
            print("Valid")
        else:
            print("Not valid")
        number//=10