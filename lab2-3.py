print("โปรดกรอกข้อมูล")
x = int(input("น้ำหนัก : "))
t = int(input("ส่วนสูง : "))
bmi = x/(t/100)**2
print("MBI = ",float(bmi))
if bmi < 18.50:
    print("อยู่ในเกณท์ : ผอม")
elif bmi >= 18.50 and bmi <= 22.90:
    print("อยู่ในเกณท์ : ปกติ")
elif bmi >= 23 and bmi <= 24.90:
    print("อยู่ในเกณท์ : ท้วม")
elif bmi >= 25 and bmi <= 29.90:
    print("อยู่ในเกณท์ : อ้วน")
else:
    print("อยู่ในเกณท์ : อ้วนมาก")
