def k(c):
    k = c + 273.15
    return k

def f(c):
    f = (9/5)*c + 32
    return f

c = int(input("รับค่าอุณหภูมิ องศาเซลเซียส: "))
print("องศาเคลริน = %.2f"% k(c))
print("องศาฟาเรนไฮส์ = %.2f"% f(c))