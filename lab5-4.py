def beforemidterm(a,b,c):
    s = a+b+c
    return s
print("คะแนนเก็บ [20] คะแนนจิตพิสัย [10] คะแนนสอบกลางภาค [20]")

g = int(input("คะแนนเก็บ: "))
j = int(input("คะแนนจิตพิสัย: "))
m = int(input("คะแนนสอบกลางภาค: "))

if g <= 20 and j <= 10 and m <= 20:
    print("คะแนนเก็บก่อนกลางภาค = %d" % beforemidterm(g, j, m))
else:
    print("โปรดกรอกตัวเลขไม่เกินที่กำหนด")





