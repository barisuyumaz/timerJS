from tkinter import *

def yaz(x):
	giris.insert(-1,str(x))
	print(x)


pencere = Tk()
pencere.geometry("250x300")

giris = Entry(font="Verdana 14 bold",width=15,justify=RIGHT)

giris.place(x=20,y=20)

b = []

for i in range(1,10):
	b.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i :yaz(x)))

sayac = 0

for i in range(3):
	for j in range(3):
		b[sayac].place(x=20+i*50,y=60+j*50)
		sayac += 1 

pencere.mainloop()
