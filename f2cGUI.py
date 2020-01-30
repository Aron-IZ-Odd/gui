from tkinter import *



def convert():
	F = float(lbl1_entry.get())
	C = (F - 32) * 5 / 9
	display["text"]=str(C)


root = Tk()
root.geometry("282x100")
root.title("Fahrenheit to Celsius")

lbl1 = Label(root, text="Enter Fahrenheit")
lbl1.grid(column=0, row=0, stick=W)


lbl2 = Label(root, text="Celsius  Temperature")
display = Label(root)
lbl2.grid(column=0, row=1, stick=W)
display.grid(row=1, column=1)



btn = Button(root, text="Convert", command=convert)
btn.grid(column=0, row=2)





lbl1_entry = Entry(root, width=20)
lbl1_entry.grid(column=1, row=0, padx=10)


mainloop()
