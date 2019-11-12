
Sum=["sum","add","adding","summation","jod","+","addition"]

subtract=["sub","ghatana","subtract","-"]

division = ["/'","bhag","devide","devided","devision","half","upon","div"]

multiplication = ["multiply","guna","gune","*","into"]

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


input_yes_no="yes"

while(input_yes_no == "yes"):
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
    else:
        print(" Sorry we could not find what you want from these expressions ")

    input_yes_no = input("Do you want continue::yes/no ")

print("!!!!!!!  Thanks for Using this Smart Calculator  !!!!!!!")
