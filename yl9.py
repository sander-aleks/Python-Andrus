a = int(input("sisesta midagi vaartus: "))
b = int(input("sisesta midagi vartus: "))
c = int(input("sisesa aluse vaartus: "))

if a + b <= c or b + c <= a or a + c <= b:
    print("sellist kolmnurka ei eksiteeri")

elif a == b and b == c:
    print("tegu on vordkylgse kolmurgaga")

elif a == b or b ==c or a == c:
    print("tegu on vordhaarse kolmnurgaga")

else:
    print("Tegu on erikylgse kolmnurgaga")