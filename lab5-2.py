def a(num):
    sum = 0
    for i in range(num):
        price = int(input("รับค่าสินค้า %d " % (i + 1)))
        sum += price
    return sum

def tax(sum):
    vat = sum*7/100
    return vat

def total(a, b, c):
    t = (a-c)+b
    return t

def d(sum):
    dis = sum*5/100
    return dis


num = int(input("จำนวนสินค้า "))
sum = a(num)
print("ราคารวม %.2f" % sum)
print("ภาษี %.2f" % tax(sum))
print("รวมภาษีเงินทั้งหมด %.2f" % total(sum, tax(sum),d(sum)))