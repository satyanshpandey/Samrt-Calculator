Sum=["sum","add","adding","summation","jod","+","addition","plus","dhan"]

subtract=["sub","ghatana","subtract","-","subtraction","minus","rin","ghata"]

division = ["/'","bhag","devide","devided","devision","half","upon","div"]

multiplication = ["multiply","guna","gune","*","into"]

HCF = ["hcf","HCF","highest common factor"]

def val_frm_txt(text):
    val = []
    char=[]
    for ch in text.split(' '):
        try:
            val.append(float(ch))
        except Exception:
            char.append(ch)
    return val,char
input_val=input("Enter what you want !")
a,b=val_frm_txt(input_val)
for ch in b:
    if(ch.lower() in Sum):
        add=0
        for i in a:
            add=add + i
        print(add)
        break
    elif(ch.lower() in subtract):
        sub = a[0]
        a[0]=0
        for i in a:
            sub = sub - i
        print(sub)
        break
    elif(ch.lower() in division):
        div = a[0]
        a[0] = 1
        for i in a:
            div = div/i
        print(div)
        break
    elif(ch.lower() in multiplication):
        mul = 1
        for i in a:
            mul=mul * i
        print(mul)
        break
else:
    print("Sorry we could not find what you want from these expressions")
input()