
Sum=["sum","add","adding","summation","jod","+","addition","plus"]

subtract=["sub","ghatana","subtract","-","minus"]

division = ["/'","bhag","devide","devided","devision","half","upon","div"]

multiplication = ["multiply","guna","gune","*","into","multiplication"]

hcf=["hcf","gcd","highest common factor","Gretest common divisor","h c f","g c d"]

lcm=["lcm","lowest common factor"," l c m "]

name=["name"]
def name(list1):
    # for ch in char.split(' '):
        return "my name is munna"


def val_frm_txt(text):
    val = []
    char=[]
    for ch in text.split(' '):
        try:
            val.append(float(ch))
        except Exception:
            char.append(ch)
    return val,char

def sum(list1):
    add = 0
    for i in list1:
        add = add + i
    return add

def sub1(list1):
    sub = list1[0]
    del list1[0]
    for i in list1:
        sub = sub - i
    return sub

def div1(list1):
    div = list1[0]
    list1[0] = 1
    for i in list1:
        div = div / i
    return div
def mul1(list1):
    mul = 1
    for i in list1:
        mul = mul * i
    return mul

def hcfcal(list1):
    from functools import reduce
    def hcf(a, b):
        for i in range(min(a, b), 0, -1):
            if (a % i == 0 and b % i == 0):
                break
        return i

    def get_hcf_for(list_of_numbers_for_hcf):
        return reduce(lambda x, y: hcf(x, y), list_of_numbers_for_hcf)

    return get_hcf_for(list1)


def lcmcal(list1):
    from functools import reduce

    list_of_numbers_to_check = list1

    def lcm(x, y):
        if (x > y):
            big_num = x
        else:
            big_num = y
        check_for = 0
        i = 1
        while (check_for != x * y):
            check_for = big_num * i
            if (check_for % x == 0 and check_for % y == 0):
                break
            i = i + 1

        return check_for

    def get_lcm_for(list1):
        return reduce(lambda x, y: lcm(x, y), list1)

    return get_lcm_for(list_of_numbers_to_check)

exit="y"
input_yes_no="y"

while(input_yes_no == "y"):
    input_val = input("Enter what you want !")
    val, operation = val_frm_txt(input_val)

    for ch in operation:
        if(ch.lower() in Sum):
            sum1=sum(val)
            print(f"The Addition of all the number's are {sum1}")
            break

        elif(ch.lower() in subtract):
            sub=sub1(val)
            print(f"The Subtraction of all the given number's are {sub}")
            break

        elif (ch.lower() in division):
            div=div1(val)
            print(f"The Division of the given number's are {div}")
            break

        elif (ch.lower() in multiplication):
            mul = mul1(val)
            print(f"The Multiplication of the given number's are {mul}")
            break

        elif (ch.lower() in hcf):
            val=list(map(int,val))
            hcf1=hcfcal(val)
            print(f"hcf of given number {val} is {hcf1}")
            break

        elif (ch.lower() in lcm):
            val=list(map(int,val))
            lcm1=lcmcal(val)
            print(f"lcm of given number {val} is {lcm1}")
            break
    else:
        print(" Sorry we could not find what you want from these expressions ")

    input_yes_no = input("Do you want continue Press 'Y' for yes and 'N' for not::y/n ")

print("!!!!!!!  Thanks for Using this Smart Calculator  !!!!!!!")