print("โปรดกรอกคะเเนน")
x = int(input("คะแนน : "))

if x > 100:
    print("กรุณากรอกข้อมูล 0-100")
elif x < 0:
    print("กรุณากรอกข้อมูล 0-100")
else:
    if x >= 80:
        print("เกรด A")
    elif x >= 70:
        print("เกรด B")
    elif x >= 60:
        print("เกรด C")
    elif x >= 50:
        print("เกรด D")
    else:
        print("เกรด F")
    

    