import math
a = int(input("Valeur de a: "))
b = int(input("Valeur de b: "))
c = int(input("Valeur de c: "))
delta = b**2 -4*a*c
alpha = -b/(2*a)
beta = -delta/(4*a)
x1 = (-b+math.sqrt(delta))/(2*a)
x2 = (-b-math.sqrt(delta))/(2*a)
print(f"racines(+/-): x1 = {x1} x2 = {x2}")
print(f"forme developpée: {a}x^2 +({b})x +({c})")
print(f"forme factorisée: {a}(x-({x1}))(x-{x2})")
print(f"forme canonique: {a}(x-({alpha}))^2 + ({beta})")
