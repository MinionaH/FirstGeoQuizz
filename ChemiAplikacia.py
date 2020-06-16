from random import randint
from tkinter import *
from tkinter import ttk,messagebox,PhotoImage
win = Tk()

#Design

win.resizable(0,0)   # rata ver shedzlon aplikaciis gadideba dapataraveba , ramac shedzleba dizaini aurios
win.title("Geography Quiz")
win.iconbitmap("img/Treetog-Junior-Earth.ico")
img = PhotoImage(file="img/background.png")
h,w = img.height(),img.width()
win.geometry(f'{w}x{h}')
background_label = Label(win, image=img, )
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # es gadavige leqciis PDF idan, gamomadga :-)


Country = ["Georgia","France","Germany","Russia","Italy","Sweden","Turkey","Japan","Spain","USA","Poland","China","Israel","UK","Brazil","Bulgaria","Canada","Costa Rica"]
Capital = ["Tbilisi","Paris","Berlin","Moscow","Rome","Stockholm","Ankara","Tokyo","Madrid","Washington","Warsaw","Beijing","Jerusalem","London","Brasilia","Sofia","Ottawa","San Jose"]
num = randint(0,17)
correct = 0

# Skip Gilakis operacia
def nextbtn():
    global Country,Capital,num
    num = randint(0,17)
    varlbl.set(Country[num])

# Submit Gilakis operacia
def submitbtn():
    global num,Country,Capital,correct
    answer = entry.get()
    if answer == Capital[num]:
        correct += 1
        yesno = messagebox.askquestion("Bingo","Your answer is correct. Do You Want To continue?") # ra moxdes Yes/No s micemis Shemdgom
        if yesno == "yes":
            num = randint(0,17)
            varlbl.set(Country[num])
            entry.set("")
            points.set(correct)
        else:
            messagebox.showinfo("Goodbye","Hopefully you'll Be Back xD,")
            exit()
    else:
        messagebox.showerror("Wrong","Your Answer is wrong, Please Try again")
        correct -= 1
        num = randint(0, 17)
        varlbl.set(Country[num])
        entry.set("")
        points.set(correct)

#Label
points = IntVar()
cor = Label(win,textvariable=points,font=("Arial black",20),fg="blue").pack(side="top")

varlbl=StringVar()
label1 = Label(win,textvariable=varlbl,fg="red",font=("Arial",30,"bold")).pack(padx=20,pady=20)
varlbl.set(Country[num])

#entry
entry = StringVar()
e1 = Entry(win,textvariable=entry,font=("Arial",20)).pack(pady=20)

#Buttons
s=ttk.Style()
s.configure("b1.TButton",font=("Arial black",20),foreground="green")
s.configure("b2.TButton",font=("Arial black",20),foreground="red")


b1 = ttk.Button(win,text="Submit",command = submitbtn,style="b1.TButton")
b1.pack(pady=20)
b1 = ttk.Button(win,text="Skip",command = nextbtn,style="b2.TButton")
b1.pack(pady=20)
messagebox.showinfo("About Game","Hello There, in This game you will see countries, Your task is to enter correct capital of theirs, if you get it wrong you will lose 1 point. Good Luck, click on Skip To start the game")
win.mainloop()