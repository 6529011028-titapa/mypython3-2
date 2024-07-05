def rectengle(w1,l1):
    area = w1 * l1
    return area

w = int(input("กว้าง: "))
l = int(input("ยาว: "))
print("พื้นที่สี่เหลี่ยม %d "% rectengle(w,l))