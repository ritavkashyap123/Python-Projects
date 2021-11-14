#Age determining machine
a=int (input("enter the age= "))

if a<=0:
    print("Invalid age")
elif 0<a<=12:
    print("You are child")
elif 13<=a<=19:
    print("You are teen")
elif 20<=a<=39:
    print("You are young")
elif 40<=a<=60:
    print("You are miiddle aged person")
else:
    print("You are wise")
