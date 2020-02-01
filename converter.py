import sys
from tkinter import *

root = Tk()
root.title("Tempature Converter")
root.geometry("450x450+400+150")
frame = Frame(root)
frame.pack()

def value1():
	q = float(num1.get())
	d=float(5/9 * (q -32)); #Celsius
	label1 = Label(root, text="The value enterd in celcious is: %.1f" % d).pack(side = BOTTOM)
	return


def value2():
	q=float(num1.get())
	d = int(q); #Fehrenhiet
	f = int(d * 9/5 + 32);
	label1 = Label(root, text="The value entered in fehrenhiet is: %.1f" % f).pack(side = BOTTOM)
	return
def value3():
	q = float(num1.get())
	d = int(q + 237); #Kelvin
	f = int(9.0 / 5.0)
	t = int(f * d);
	label1 = Label(root, text="The value entered in Kelvin is: %.1f" % t).pack(side = BOTTOM)



num1 = StringVar()
cbtn = StringVar()
cbtn.set(None)


frame1 = Frame(root)
frame1.pack(side = TOP)

label2 = Label(frame1, text="Enter Tempature for Conversion", fg="black", relief = RAISED)
label2.pack(side = TOP)

label2 = Label(frame1, text="\n\n")
label2.pack(side = TOP)

display = Entry(frame1, textvariable = num1, bd=30, insertwidth = 1, font=12, justify = "center")
display.pack(side = TOP)

radio1 = Radiobutton(frame1, text="Celsius", variable= cbtn, value="Celsius", command=value1).pack(side = BOTTOM)
radio1 = Radiobutton(frame1, text="Fehrenhiet", variable = cbtn, value="Fehrenhiet", command=value2).pack(side = BOTTOM)
radio1 = Radiobutton(frame1, text="Kelvin", variable = cbtn, value="Kelvin",command=value3).pack(side = BOTTOM)
button1 = Button(frame1, padx=16, pady=16, bd=8, text="Convert", fg="black", font=48,command=value1)
button1.pack(side = BOTTOM)
root.mainloop()
