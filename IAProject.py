from tkinter import *

mrnList = ["D24245", "yolo"]
idList = ["debi", "you"]


def users():
    username = []


def loginScreen():
    logScreen = Toplevel(form)
    logScreen.title("Patient File")
    logScreen.geometry("300x250")

    Label(logScreen, text="Fill the information below for this patient").pack()
    Label(logScreen, text="New MRN Number: ").pack()

    # mrnKey = input()


def patientAdd():
    registerScreen = Toplevel(form)
    registerScreen.title("New Patient")
    registerScreen.geometry("300x250")

    mrnRegister = StringVar()
    idRegister = StringVar()
    mrnNewKeys = mrnRegister.get()
    idVerify = idRegister.get()

    Label(registerScreen, text="Fill the information below for registering a new patient:").pack()

    mrn_label = Label(registerScreen, text="New MRN Number:").pack()
    mrn_input = Entry(registerScreen, textvariable=mrnRegister).pack()

    id_label = Label(registerScreen, text="ID Number:").pack()
    id_input = Entry(registerScreen, textvariable=idRegister, show='*').pack()

    Button(registerScreen, text="Register", width=10, height=1, command=users).pack()


# Startup screen
form = Tk()
form.geometry("500x400")
form.title("Mount Sinai Patient Site")
Label(text="Patient File Portal", font=("Arial", 15)).pack()

mrn = StringVar()  # (form, idList) window, values
id = StringVar()
mrnKeys = mrn.get()
idKeys = id.get()

mrn_label = Label(form, text="MRN Number:").pack()
mrn_input = Entry(form, textvariable=mrn).pack()

id_label = Label(form, text="ID Number:").pack()
id_input = Entry(form, textvariable=id).pack()
logBtn = Button(text="Login", height="2", width="30").pack()

if mrnKeys in mrnList and idKeys in idList:
    logBtn = Button(text="Login", height="2", width="30", command=loginScreen).pack()

elif mrnKeys == "" and idKeys == "":
    print("no")

Button(text="Add New Patient", height="2", width="30", command=patientAdd).pack()

mainloop()
