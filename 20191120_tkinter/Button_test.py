from tkinter import *

root=Tk()
root.minsize(400,500)

# 数字键
btn1=Button(text='1')
btn1.grid(row=3,column=0,ipadx=15,ipady=10,padx=3,pady=3)
btn2=Button(text='2')
btn2.grid(row=3,column=1,ipadx=15,ipady=10,padx=3,pady=3)
btn3=Button(text='3')
btn3.grid(row=3,column=2,ipadx=15,ipady=10,padx=3,pady=3)
btn4=Button(text='4')
btn4.grid(row=2,column=0,ipadx=15,ipady=10,padx=3,pady=3)
btn5=Button(text='5')
btn5.grid(row=2,column=1,ipadx=15,ipady=10,padx=3,pady=3)
btn6=Button(text='6')
btn6.grid(row=2,column=2,ipadx=15,ipady=10,padx=3,pady=3)
btn7=Button(text='7')
btn7.grid(row=1,column=0,ipadx=15,ipady=10,padx=3,pady=3)
btn8=Button(text='8')
btn8.grid(row=1,column=1,ipadx=15,ipady=10,padx=3,pady=3)
btn9=Button(text='9')
btn9.grid(row=1,column=2,ipadx=15,ipady=10,padx=3,pady=3)
btnb=Button(text='%')
btnb.grid(row=4,column=0,ipadx=13,ipady=10,padx=3,pady=3)
btn0=Button(text='0')
btn0.grid(row=4,column=1,ipadx=15,ipady=10,padx=3,pady=3)
btnd=Button(text='.')
btnd.grid(row=4,column=2,ipadx=17,ipady=10,padx=3,pady=3)

# 运算符
btnC=Button(text='C')
btnC.grid(row=0,column=0,ipadx=15,ipady=10,padx=3,pady=3)
btn_divide=Button(text='÷')
btn_divide.grid(row=0,column=1,ipadx=14,ipady=10,padx=3,pady=3)
btn_multiply=Button(text='X')
btn_multiply.grid(row=0,column=2,ipadx=15,ipady=10,padx=3,pady=3)
btn_Backspace=Button(text='←')
btn_Backspace.grid(row=0,column=3,ipadx=16,ipady=10,padx=3,pady=3)
btn_subtract=Button(text='-')
btn_subtract.grid(row=1,column=3,ipadx=19,ipady=10,padx=3,pady=3)
btn_add=Button(text='+')
btn_add.grid(row=2,column=3,ipadx=17,ipady=10,padx=3,pady=3)
btn_equal=Button(text='=')
btn_equal.grid(row=3,column=3,ipadx=17,ipady=38,padx=3,pady=3,rowspan=2)

# 显示窗口

btn_print=Button(root,text='显示区域')
btn_print.place(x=3,y=300,width=220,height=50)

btn_rel=Button(root,text="相对位置")
btn_rel.place(relx=0.2,rely=0.2,relwidth=0.3,relheight=0.3)

root.mainloop()