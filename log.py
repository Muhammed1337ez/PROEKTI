from tkinter import Tk, Frame, LabelFrame, Label, Entry, Button, messagebox, Spinbox
from tkinter.ttk import Combobox
from dbase import Database

window = Tk()
window.geometry("600x700")
window.configure(bg="lime")
db = Database()

# ============================================================
frame = Frame(window)
frame.grid(padx=103, pady=35)

label_frame = LabelFrame(frame, bg="white")
label_frame.grid()


# ==================================================================
registration_label = Label(label_frame, text="Ro'yhatdan oting",
                        fg="lime", bg="white",
                        font=("Verdana", 30))
registration_label.grid(row=0, column=0, ipadx=40, columnspan=2, sticky="news")

# ============================================================
firstname_label = Label(label_frame, text="Ismingiz",
                        fg="lime", bg="white",
                        font=("Verdana", 17))
firstname_label.grid(row=1, column=0)
firstname_entry = Entry(label_frame, bg="lime")
firstname_entry.grid(row=2, column=0,ipadx=17, ipady=6)


lastname_label = Label(label_frame, text="Familyangiz",
                        fg="lime", bg="white",
                        font=("Verdana", 17))
lastname_label.grid(row=1, column=1)
lastname_entry = Entry(label_frame, bg="lime")
lastname_entry.grid(row=2, column=1,ipadx=17, ipady=6)

# ==================================================
emailadress_label = Label(label_frame, text="Email",
                        fg="lime", bg="white",
                        font=("Verdana", 17))
emailadress_label.grid(row=3, column=0)
emailadress_entry = Entry(label_frame, bg="lime")
emailadress_entry.grid(row=4, column=0, ipadx=40,ipady=6, columnspan=2, sticky="news")

# =============================================
country_label = Label(label_frame, text="Country",
                        fg="lime", bg="white",
                        font=("Verdana", 17))
country_label.grid(row=5, column=0)
combo_country = Combobox(label_frame,
                         values=["Uzbekistan", "Turkiye",
                                 "USA", "Phalastine",
                                 "Russian", "China"])
combo_country.grid(row=6, column=0, ipadx=40, columnspan=2, sticky="news")

# =======================================================
age_label = Label(label_frame, text="Age",
                        fg="lime", bg="white",
                        font=("Verdana", 17))
age_label.grid(row=7, column=0)

age_spinbox = Spinbox(label_frame, from_=0, to=99, bg="lime")
age_spinbox.grid(row=8, column=0,ipadx=17, ipady=6)

# =======================================================
phonenumber_label = Label(label_frame, text="Raqamingiz",
                        fg="lime", bg="white",
                        font=("Verdana", 17))
phonenumber_label.grid(row=7, column=1)
phonenumber_entry = Entry(label_frame, bg="lime")
phonenumber_entry.grid(row=8, column=1,ipadx=17, ipady=6)


# ====================================================
def register_func3():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    emailadress = emailadress_entry.get()
    phonenumber = phonenumber_entry.get()
    if firstname and lastname and emailadress and phon enumber:
        db.insert_user(firstname=firstname, lastname=lastname, emailadress=emailadress, phonenumber=phonenumber)
        messagebox.showinfo(title="Saqlandi !",
                            message="Siz muvaffaqiyatli ro'yhatdan o'tdingiz !")
    else:
        messagebox.showerror(title="Xato",
                             message="Noto'g'ri kiritish !")


# =====================================================
registor_button = Button(label_frame, text="Register",
                         fg="lime", bg="white",
                         font=("Verdana", 17),
                         command=register_func3)
registor_button.grid(row=9, column=0, ipadx=40, columnspan=2, sticky="news")
for widget in label_frame.winfo_children():
    widget.grid_configure(padx=15, pady=8)

































































window.mainloop()