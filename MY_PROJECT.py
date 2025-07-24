from tkinter import *
from tkinter import ttk 
import tkinter as tk
from time import strftime
from tkinter import messagebox


class Customer:
    def __init__(self,main):
        self.main = main
        self.Title_Frame = Frame(self.main,height=70,width=1200,background="#2c3e50",bd=2,relief=GROOVE)
        self.Title_Frame.pack()

        self.Title = Label(self.Title_Frame,text="Hotel Management System",font=("Calibri", 18, "bold"),width=1200,bg="#2c3e50",fg="white")
        self.Title.pack()

        self.Frame_3 = Frame(self.main,height=70,width=540,bd=5,relief=GROOVE,bg="gray")
        self.Frame_3.place(x=1,y=0)
        self.Frame_3.pack_propagate(0)

        self.Frame_4 = Frame(self.main,height=70,width=540,bd=5,relief=GROOVE,bg="gray")
        self.Frame_4.place(x=825,y=0)
        self.Frame_4.pack_propagate(0)


        self.Frame_1 = Frame(self.main,height=640,width=500,bd=10,relief=GROOVE,bg="lightgreen")
        self.Frame_1.place(x=0,y=110)
        self.Frame_1.pack_propagate(0)

        Label(self.Frame_1,text="Customer Details",bg="orange",fg="white",bd=2,font="arial 13 bold").place(x = 20 , y=20)

        self.Room_no = Label(self.Frame_1,text ="Room no:",bg="Lightgrey",font="arial 11 bold")
        self.Room_no.place(x=30,y=60)

        self.Room_no_Entry = Entry(self.Frame_1,width=40)
        self.Room_no_Entry.place(x=150,y=60)

        self.Name = Label(self.Frame_1, text="Name:", bg="Lightgrey", font="arial 11 bold")
        self.Name.place(x=30, y=100)

        self.Name_Entry = Entry(self.Frame_1, width=40)
        self.Name_Entry.place(x=150, y=100)

        self.No_of_people = Label(self.Frame_1, text="No of people:", bg="Lightgrey", font="arial 11 bold")
        self.No_of_people.place(x=30, y=140)

        self.No_of_people_Entry = Entry(self.Frame_1, width=40)
        self.No_of_people_Entry.place(x=150, y=140)

        self.Address = Label(self.Frame_1, text="Address:", bg="Lightgrey", font="arial 11 bold")
        self.Address.place(x=30, y=180)

        self.Address_Entry = Entry(self.Frame_1, width=40)
        self.Address_Entry.place(x=150, y=180)

        self.Check_in = Label(self.Frame_1, text="Checkin date:", bg="Lightgrey", font="arial 11 bold")
        self.Check_in.place(x=30, y=220)

        self.Check_in_Entry = Entry(self.Frame_1, width=40)
        self.Check_in_Entry.place(x=150, y=220)

        self.Check_out = Label(self.Frame_1, text="Checkout date:", bg="Lightgrey", font="arial 11 bold")
        self.Check_out.place(x=30, y=260)

        self.Check_out_Entry = Entry(self.Frame_1, width=40)
        self.Check_out_Entry.place(x=150, y=260)
        self.Room = Label(self.Frame_1, text="Room:", bg="Lightgrey", font="arial 11 bold")
        self.Room.place(x=30, y=300)

        ac_non_ac_var = tk.StringVar(value="NONE")
        ac_radio = tk.Radiobutton(self.Frame_1, text="AC", variable=ac_non_ac_var, value="AC")
        ac_radio.place(x=150, y=300)
        non_ac_radio = tk.Radiobutton(self.Frame_1, text="Non-AC", variable=ac_non_ac_var, value="Non-AC")
        non_ac_radio.place(x=200, y=300)

        self.By = Label(self.Frame_1, text="Registered by:", bg="Lightgrey", font="arial 11 bold")
        self.By.place(x=30, y=345)

        lists = [ "Staff 1", "Staff 2" ,"Staff 3", "Staff 4", "Staff 5"]
        listroom = StringVar(main)

        listroom.set("Choose:")
        menu = OptionMenu(self.Frame_1, listroom, *lists)
        menu.place(x=150, y=340)
        c=IntVar()
        ch=Checkbutton(self.Frame_1,text="VERIFIED",variable=c)
        ch.place(x=250,y=342)

        #############################BUTTONS###################################


        self.Button_Frame = Frame(self.Frame_1,height=220,width=280,relief=GROOVE,bd=2,bg="Lightgrey")
        self.Button_Frame.place(x = 90, y = 380)

        self.Add = Button(self.Button_Frame,text="Add",width=15,font=("Calibri", 16, "bold"), fg="white",command=self.Add,bg="#2980b9")
        self.Add.pack()

        self.Delete = Button(self.Button_Frame, text="Delete",width=15,font=("Calibri", 16, "bold"), fg="white", bg="#c0392b",command=self.Delete)
        self.Delete.pack()

        self.Update = Button(self.Button_Frame, text="Update",width=15,font=("Calibri", 16, "bold"), fg="white",bg="#f39c12",command=self.Update)
        self.Update.pack()

        self.Clear = Button(self.Button_Frame, text="Clear",width=15,font=("Calibri", 16, "bold"), fg="white", bg="#16a085",command=self.Clear)
        self.Clear.pack()

        self.Exit = Button(self.Button_Frame, text="Exit",width=15,font=("Calibri", 16, "bold"), fg="white", bg="red",command=self.on_exit)
        self.Exit.pack()


        self.Frame_2 = Frame(self.main, height=640, width=1400, bd=10, relief=GROOVE, bg="lightblue")
        self.Frame_2.place(x=500,y=110)


        self.tree = ttk.Treeview(self.Frame_2,column=("c1","c2","c3","c4","c5","c6"),show="headings",height=30)

        self.tree.column("#1",anchor=CENTER,width=80)
        self.tree.heading("#1",text="Room no",)

        self.tree.column("#2", anchor=CENTER, width=120)
        self.tree.heading("#2", text="Name")

        self.tree.column("#3", anchor=CENTER, width=140)
        self.tree.heading("#3", text="No of people")

        self.tree.column("#4", anchor=CENTER, width=150)
        self.tree.heading("#4", text="Address")


        self.tree.column("#5", anchor=CENTER, width=170)
        self.tree.heading("#5", text="Checkin date")

        self.tree.column("#6", anchor=CENTER, width=180)
        self.tree.heading("#6", text="Checkout date")

        self.tree.insert("", index=0, values=(101, "Nick", 2, "123,car street Erode", "10-05-2024", "12-05-2024"))

        self.tree.pack()
        self.tree.insert("", index=1, values=(102, "Mani", 2, "123,ANNAI NAGAR 3rd street DINDIGUL", "17-05-2024", "19-05-2024"))

        self.tree.pack()
        self.tree.insert("", index=3, values=(103, "Siva", 2, "123,PERIYAR NAGAR 2nd CROSS street Erode", "20-05-2024", "22-05-2024"))

        self.tree.pack()



    def Add(self):
        Room_no = self.Room_no_Entry.get()
        Name = self.Name_Entry.get()
        No_of_people = self.No_of_people_Entry.get()
        Address = self.Address_Entry.get()
        Checkin_date = self.Check_in_Entry.get()
        Checkout_date = self.Check_out_Entry.get()

        if not Room_no.isdigit() or int(Room_no) <= 0:
            messagebox.showerror("Error", "Please enter a valid Room no.")
            return
        
        if not No_of_people.isdigit() or int(No_of_people) <= 0:
            messagebox.showerror("Error", "Please enter a Number of people are want to stay.")
            return
        

        self.tree.insert("", index=0, values=(Room_no, Name, No_of_people, Address, Checkin_date, Checkout_date))
        messagebox.showinfo("Success", "Record Added Successfully")

    def Delete(self):
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)["values"][0]
        print(selected_item)
        self.tree.delete(item)

        messagebox.showinfo("Delete", "Record Deleted Successfully")

    def Update(self):
        Room_no = self.Room_no_Entry.get()
        Name = self.Name_Entry.get()
        No_of_people = self.No_of_people_Entry.get()
        Address = self.Address_Entry.get()
        Checkin_date = self.Check_in_Entry.get()
        Checkout_date = self.Check_out_Entry.get()

        item = self.tree.selection()[0]
        self.tree.item( item, values=(Room_no, Name, No_of_people, Address, Checkin_date, Checkout_date))

        messagebox.showinfo("Success", "Record Updated Successfully")

    def Clear(self):
        self.Room_no_Entry.delete(0, END)
        self.Name_Entry.delete(0, END)
        self.No_of_people_Entry.delete(0, END)
        self.Address_Entry.delete(0, END)
        self.Check_in_Entry.delete(0, END)
        self.Check_out_Entry.delete(0, END)
        
        messagebox.showinfo("Clear", "Record Cleared Successfully")
    
    def on_exit(self):
        main.destroy()

main = Tk()
main.title("Hotel Management System")
main.resizable(False, False)
main.geometry("1920x1080+0+0")
main.state("zoomed")


def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(main, font=('calibri', 40, 'bold'),
			background='lightgreen',
			foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack()
time()
Customer(main)
main.geometry('600x800') 
main.mainloop()