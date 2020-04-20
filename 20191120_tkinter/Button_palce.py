from tkinter import *

root=Tk()
root.maxsize(1000,1000)
root.minsize(500,500)

# 绝对位置
btn1=Button(text='按钮1')
btn1.place(x= 100 ,y =100 ,width = 50 ,heigh=50)



# 相对位置

btn2=Button(text='按钮2')
btn2.place(relx=0.1,rely=0.1,relwidth=0.2,relheigh=0.2)

root.mainloop()