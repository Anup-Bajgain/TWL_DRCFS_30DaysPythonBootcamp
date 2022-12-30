#calculator

#basic arithmetic calculation

#defining the function for operator
def add(x,y) -> float:
            result = x + y
            return result

def sub(x,y) ->float:
            result = x - y
            return result

def mul(x,y) -> float:
        result = x * y
        return result

def div(x,y) -> float:
        result = x/y
        return result 

def root(x,y) -> float:

        result = x**(1/y)
        return result

def power(x,y) ->float:
        result = x**y
        return result

def isValidInt(input):
    if input[0] == '_':
        return input[1:].isdigit()
    else:
        return input.isdigit()


#ask to select any option
print('choose one of the following option:\n 1.addition of two number\t 2.subtraction of two number\n 3.multiplication of two number\t 4. division of one number by another \n 5.nth root of a number \t 6.nth power of number ')
opn = input('Enter your choice here: ')

check = isValidInt(opn)

if check is True:
    opn = int(opn)
    print('-' * 60)
    if opn == 1:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        print(n1, "+" ,n2,"=",add(n1,n2))

    elif opn == 2:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        print(n1, "-" ,n2,"=",sub(n1,n2))
        
    elif opn == 3:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        print(n1, "*" ,n2,"=",mul(n1,n2))

    elif opn == 4:
        n1 = float(input("Enter the Dividend: "))
        n2 = float(input("Enter the Divisor: "))
        print(n1, "/" ,n2,"=",div(n1,n2))

    elif opn == 5:
        n1 = float(input("Enter the base: "))
        n2 = int(input("Enter the radicand: "))
        if n2==2:
            print(f"squareroot of { n1} =",root(n1,n2))
        elif n2==3:
            print(f"cuberoot of { n1} =",root(n1,n2))
        else:
            print(f"{n2}th root of { n1} =",root(n1,n2))

    elif opn == 6:
        n1 = float(input("Enter the base: "))
        n2 = float(input("Enter the power: "))
        if n2==2:
            print(f"square of { n1} =",power(n1,n2))
        elif n2==3:
            print(f"cube of { n1} =",power(n1,n2))
        else:
            print(f"{n2}th root of { n1} =",power(n1,n2))

    else:
        print("invalid option")

    print('-' * 60)

else:
    print("Input integer value")