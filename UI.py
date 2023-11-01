import tkinter as tk
from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import *
from machineLearning import *

#--------------------------UTILITY FUNCTIONS------------------------>>>>>>>>
#LOGIN FUNCTION
def loginBtn():
    username = username_entry.get()
    password = password_entry.get()

    if isUserPresent(username, password): #returns true or false 
        welcomeHeading.configure(text=f"Welcome {username}")

        login_frame.pack_forget() 
        home_frame.pack(expand=True, fill=tk.BOTH)      
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def registerBtn():
    login_frame.pack_forget()
    register_frame.pack(expand=True, fill=tk.BOTH)

def signUpBtn():
    username = register_username_entry.get()
    password = register_password_entry.get()
    mobile = register_mobile_entry.get()
    email = register_email_entry.get()

    if(username == "" or password == ""):
        return 

    createAccount(username, password, mobile, email)

    welcomeHeading.configure(text=f"Welcome {username}")

    register_frame.pack_forget()
    home_frame.pack(expand=True, fill=tk.BOTH)    

#FORGOT PASSWORD FUNCTION
def forgotPasswordBtn():
    login_frame.pack_forget()
    forgot_frame.pack(expand=True, fill=tk.BOTH)

#VALIDATE CREDENTIALS IF PASSWORD FORGOTTEN
def validateBtn():
    username = forgot_username_entry.get()
    mobile = forgot_mobile_entry.get()
    email = forgot_email_entry.get()

    if isCredentialsCorrect(username, mobile, email): #match the credentials
        forgot_frame.pack_forget()
        change_frame.pack(expand=True, fill=tk.BOTH)

    else:
        messagebox.showerror("Error", "Incorrect Credentials.")

#CHANGE PASSWORD
def changeBtn():
    username = forgot_username_entry.get()
    newPassword = change_password_entry.get()
    changePassword(username, newPassword)

    welcomeHeading.configure(text=f"Welcome {username}")
    change_frame.pack_forget()
    home_frame.pack(expand=True, fill=tk.BOTH)    

#PREDICT AND UPDATE THE OUTPUT TEXT
def predictBtn():
    response = predict()
    outputHeading.configure(text=f"Tomorrow's temperature for Day{response[0]} is  {response[1]} \u00b0C", font=("aerial", 40))

#DATASET
def showData():
    data = getData()
    outputHeading.configure(text=f"{data}", font=("aerial", 20))
    print(data)

def addingData():
    res = addData(temp_entry.get())
    outputHeading.configure(text=f"{res}", font=("aerial", 30))

def updatingData():
    res = updateData(day_entry.get(), temp_entry.get())
    outputHeading.configure(text=f"{res}", font=("aerial", 30))

def deletingData():
    res = deleteData(day_entry.get())
    outputHeading.configure(text=f"{res}", font=("aerial", 30))



# ---------------------------------FRAMES--------------------------------->>>>>>>>>
# MAIN 
root = CTk()
set_default_color_theme("asset/themes/theme4.json")
root.geometry("1920x1080")
root.title("Login Page")
root.iconbitmap("asset/icon.ico")

# LOGIN
login_frame = CTkFrame(master=root)

heading=CTkLabel(master=login_frame, width=1000, height=100, text="Temperature Predictor ☀️", font=("aerial", 72), text_color="white")
heading.place(anchor="center", relx=0.5, rely=0.2)

username_entry = CTkEntry(master=login_frame, width=500, height=50, placeholder_text="Username")
username_entry.place(rely = 0.35, relx=0.5,anchor="center")

password_entry = CTkEntry(master=login_frame, width=500, height=50, show="*", placeholder_text="Password")
password_entry.place(rely = 0.4, relx=0.5, anchor="center")

login_button = CTkButton(master=login_frame, text="Login", command=loginBtn)
login_button.place(rely = 0.47, relx=0.5, anchor="center")

register_button = CTkButton(master=login_frame, text="Register", command=registerBtn)
register_button.place(rely = 0.51, relx=0.5, anchor="center")

forgot_button = CTkButton(master=login_frame, text="Forgot Password?", command=forgotPasswordBtn)
forgot_button.place(rely = 0.55, relx=0.5, anchor="center")


#REGISTER 
register_frame = CTkFrame(master=root)

registerHeading=CTkLabel(master=register_frame, width=1000, height=100, text="Register", font=("aerial", 72), text_color="white")
registerHeading.place(anchor="center", relx=0.5, rely=0.2)

register_username_entry = CTkEntry(master=register_frame, width=500, height=50, placeholder_text="Username")
register_username_entry.place(rely = 0.35, relx=0.5,anchor="center")

register_password_entry = CTkEntry(master=register_frame, width=500, height=50, placeholder_text="Password")
register_password_entry.place(rely = 0.4, relx=0.5,anchor="center")

register_mobile_entry = CTkEntry(master=register_frame, width=500, height=50, placeholder_text="Mobile Number")
register_mobile_entry.place(rely = 0.45, relx=0.5,anchor="center")

register_email_entry = CTkEntry(master=register_frame, width=500, height=50, placeholder_text="Email")
register_email_entry.place(rely = 0.5, relx=0.5,anchor="center")

signUp_button = CTkButton(master=register_frame, text="Sign Up", command=signUpBtn)
signUp_button.place(rely = 0.55, relx=0.5, anchor="center")


#FORGOT PASSWORD
forgot_frame = CTkFrame(master=root)

registerHeading=CTkLabel(master=forgot_frame, width=1000, height=100, text="Enter Credentials", font=("aerial", 72), text_color="white")
registerHeading.place(anchor="center", relx=0.5, rely=0.2)

forgot_username_entry = CTkEntry(master=forgot_frame, width=500, height=50, placeholder_text="Username")
forgot_username_entry.place(rely = 0.35, relx=0.5,anchor="center")

forgot_mobile_entry = CTkEntry(master=forgot_frame, width=500, height=50, placeholder_text="Mobile")
forgot_mobile_entry.place(rely = 0.4, relx=0.5,anchor="center")

forgot_email_entry = CTkEntry(master=forgot_frame, width=500, height=50, placeholder_text="Email")
forgot_email_entry.place(rely = 0.45, relx=0.5,anchor="center")

validate_button = CTkButton(master=forgot_frame, text="Sign Up", command=validateBtn)
validate_button.place(rely = 0.55, relx=0.5, anchor="center")

#CHANGE PASSWORD
change_frame = CTkFrame(master=root)

changeHeading=CTkLabel(master=change_frame, width=1000, height=100, text="Set New Password", font=("aerial", 72), text_color="white")
changeHeading.place(anchor="center", relx=0.5, rely=0.2)

change_password_entry = CTkEntry(master=change_frame, width=500, height=50, placeholder_text="New Password")
change_password_entry.place(rely = 0.4, relx=0.5,anchor="center")

change_button = CTkButton(master=forgot_frame, text="Change", command=validateBtn)
change_button.place(rely = 0.55, relx=0.5, anchor="center")

# HOME 
home_frame = CTkFrame(master=root)

welcomeHeading=CTkLabel(master=home_frame, width=1000, height=100, text="Welcome", font=("aerial", 72), text_color="white")
welcomeHeading.place(anchor="center", relx=0.5, rely=0.1)

day_entry = CTkEntry(master=home_frame, width=300, height=50, placeholder_text="Enter the Day Number: ", font=("aerial", 20))
day_entry.place(rely = 0.2, relx=0.4,anchor="center")

temp_entry = CTkEntry(master=home_frame, width=300, height=50, placeholder_text="Enter the Temperature: ", font=("aerial", 20))
temp_entry.place(rely = 0.2, relx=0.6,anchor="center")

add_button = CTkButton(master=home_frame, text="ADD to dataset", height = 50, command=addingData)
add_button.place(rely = 0.3, relx=0.4, anchor="center")

update_button = CTkButton(master=home_frame, text="UPDATE in dataset", height = 50, command=updatingData)
update_button.place(rely = 0.3, relx=0.5, anchor="center")

delete_button = CTkButton(master=home_frame, text="DELETE from dataset", height = 50, command=deletingData)
delete_button.place(rely = 0.3, relx=0.6, anchor="center")

predict_button = CTkButton(master=home_frame, text="PREDICT", command=predictBtn, width = 400, height=50)
predict_button.place(rely = 0.42, relx=0.5, anchor="center")

plot_button = CTkButton(master=home_frame, text="PLOT", command=plotDataFromDataset, width = 400, height=50)
plot_button.place(rely = 0.49, relx=0.5, anchor="center")

show_button = CTkButton(master=home_frame, text="SHOW DATA", command=showData, width = 400, height=50)
show_button.place(rely = 0.56, relx=0.5, anchor="center")

outputHeading=CTkLabel(master=home_frame, width=1000, height=100, text="Tomorrow's Temperature: ", font=("aerial", 50), text_color="white")
outputHeading.place(anchor="center", relx=0.5, rely=0.7)

#----------------------------INITIALIZING--------------------->>>>>>>>>>>>>
createTable()
createDataset()
login_frame.pack(expand=True, fill=tk.BOTH)
root.mainloop()
# clearDataset()