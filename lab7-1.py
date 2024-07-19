import tkinter as tk
app = tk.Tk()
app.geometry("500x300")

def showme():
    se1 = e1.get()
    se2 = e2.get()
    print(se1)
    print(se2)
   

app.title('Design by nina')
l1 = tk.Label(text='ยินดีต้อนรับเเข้าสู่ Python')
l2 = tk.Label(text='sleep')
l3 = tk.Label(text='กรอกชื่อสินค้า:')
e1 = tk.Entry()
l4 = tk.Label(text='ราคาสินค้า:')
e2 = tk.Entry()

b1 = tk.Button(text="ตกลง", command= showme)

#l1.pack()
#l1.grid()

l1.place(x=50, y=10)

l2.place(x=50, y=50)

l3.place(x=20, y=70)
e1.place(x = 100,y=70)

l4.place(x=40, y=100)
e2.place(x = 100,y=100)

b1.place(x = 100,y=130)

