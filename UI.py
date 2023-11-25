import tkinter as tk
from captcha.image import ImageCaptcha
import random
from customtkinter import *
from PIL import Image
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

#--------------------------------------------------------------->>>>>>>>>>
#ADMIN FUNCTION
def adminLoginBtn():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "123":
        login_frame.pack_forget() 
        admin_frame.pack(expand=True, fill=tk.BOTH)      
    else:
        messagebox.showerror("Login Failed", "Invalid Admin username or password")

# ------------------------------------------------->>>>>>>>>>>>>>>
def userInfoBtn():
    str = "   ID     NAME     PASSWORD     PH.NO     EMAIL\n\n"
    data = showUserData()
    for record in data:
        str += f"{record}\n"

    # outputHeading.configure(text=f"{data}", font=("aerial", 20))

    dataWindow = tk.Toplevel(root)
    dataLabel=CTkLabel(master=dataWindow, width=1000, height=100, text=str, font=("aerial", 50), text_color="black")
    dataLabel.place(anchor="center", relx=0.5, rely=0.2)
    dataLabel.pack()

    print(data)

# ------------------------------------------------->>>>>>>>>>>>>>>
def auditTableBtn():
    str = "   ID     TEMPERATURE     OPERATION     DATE     TIME\n\n"
    data = getDatasetAudit()
    for record in data:
        str += f"{record}\n"

    # outputHeading.configure(text=f"{data}", font=("aerial", 20))

    dataWindow = tk.Toplevel(root)
    dataLabel=CTkLabel(master=dataWindow, width=1000, height=100, text=str, font=("aerial", 50), text_color="black")
    dataLabel.place(anchor="center", relx=0.5, rely=0.2)
    dataLabel.pack()

    print(data)


# ------------------------------------------------------->>>>>>>>>>>>>>
#CAPTCHA GENERATING FUNCTION
def generateCaptcha():

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"

    total = nums+lower+upper
    chars = "".join(random.sample(total, 6))

    capObj = ImageCaptcha(height=150, width=250)
    capObj.write(chars=chars, output="asset/captcha/cap.png")

    print(chars)
    return chars


#REGISTER BUTTON
def registerBtn():
    login_frame.pack_forget()
    register_frame.pack(expand=True, fill=tk.BOTH)

def signUpBtn():
    username = register_username_entry.get()
    password = register_password_entry.get()
    mobile = register_mobile_entry.get()
    email = register_email_entry.get()
    captcha = cap_entry.get()

    if(captcha != chars):
        print("Incorrect Captcha Letters")
        register_error.configure(text = "Incorrect Captcha Letters!")
        return

    if(username == "" or password == "" or mobile == "" or email == ""):
        print("Fill All the entries")
        register_error.configure(text = "Fill All the entries!")
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

#DATASET-------------------------------------------------------->>>>>>>>>>
def showData():
    str = "   Day     Temperature\n\n"
    data = getData()
    for record in data:
        str += f"{record[0]} \t {record[1]}\n"

    # outputHeading.configure(text=f"{data}", font=("aerial", 20))

    dataWindow = tk.Toplevel(root)
    dataLabel=CTkLabel(master=dataWindow, width=1000, height=100, text=str, font=("aerial", 50), text_color="black")
    dataLabel.place(anchor="center", relx=0.5, rely=0.2)
    dataLabel.pack()

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

#NAVIGATION------------------------------->>>>>>>>>>>>>
def adminToLogin():
    admin_frame.pack_forget()
    login_frame.pack(expand=True, fill=tk.BOTH)

def registerToLogin():
    register_frame.pack_forget()
    login_frame.pack(expand=True, fill=tk.BOTH)

def forgotToLogin():
    forgot_frame.pack_forget()
    login_frame.pack(expand=True, fill=tk.BOTH)

def changeToLogin():
    change_frame.pack_forget()
    login_frame.pack(expand=True, fill=tk.BOTH)

def homeToLogin():
    home_frame.pack_forget()
    login_frame.pack(expand=True, fill=tk.BOTH)

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

admin_button = CTkButton(master=login_frame, text="Admin Login", command=adminLoginBtn)
admin_button.place(rely = 0.59, relx=0.5, anchor="center")


# ADMIN
admin_frame = CTkFrame(master=root)

admin_to_login_button = CTkButton(master=admin_frame, text="\u2190", width=10, height=50, corner_radius=100, command=adminToLogin)
admin_to_login_button.place(rely = 0.05, relx=0.05, anchor="center")

adminHeading=CTkLabel(master=admin_frame, width=1000, height=100, text="Admin Panel", font=("aerial", 72), text_color="white")
adminHeading.place(anchor="center", relx=0.5, rely=0.1)

userInfo_button = CTkButton(master=admin_frame, text="User Info", command=userInfoBtn, height= 100)
userInfo_button.place(rely = 0.5, relx=0.4, anchor="center")

auditTable_button = CTkButton(master=admin_frame, text="Audit Table", command=auditTableBtn, height= 100)
auditTable_button.place(rely = 0.5, relx=0.6, anchor="center")


#REGISTER 
register_frame = CTkFrame(master=root)

back_to_login_button = CTkButton(master=register_frame, text="\u2190", width=10, height=50, corner_radius=100, command=registerToLogin)
back_to_login_button.place(rely = 0.05, relx=0.05, anchor="center")

registerHeading=CTkLabel(master=register_frame, width=1000, height=100, text="Register", font=("aerial", 72), text_color="white")
registerHeading.place(anchor="center", relx=0.5, rely=0.1)

register_username_entry = CTkEntry(master=register_frame, width=500, height=50, placeholder_text="Username")
register_username_entry.place(rely = 0.25, relx=0.5,anchor="center")

register_password_entry = CTkEntry(master=register_frame, width=500, height=50, placeholder_text="Password")
register_password_entry.place(rely = 0.3, relx=0.5,anchor="center")

register_mobile_entry = CTkEntry(master=register_frame, width=500, height=50, placeholder_text="Mobile Number")
register_mobile_entry.place(rely = 0.35, relx=0.5,anchor="center")

register_email_entry = CTkEntry(master=register_frame, width=500, height=50, placeholder_text="Email")
register_email_entry.place(rely = 0.4, relx=0.5,anchor="center")

# captcha inside register---------------------------->>>
chars = generateCaptcha()
path = "asset/captcha/cap.png"
i = CTkImage(light_image=Image.open(path), size=(250,100))

cap=CTkLabel(master=register_frame, width=1000, height=100, image=i, text="")
cap.place(anchor="center", relx=0.5, rely=0.5)

cap_entry = CTkEntry(master=register_frame, width=250, height=30, placeholder_text="Captcha:")
cap_entry.place(rely = 0.57, relx=0.5,anchor="center")

signUp_button = CTkButton(master=register_frame, text="Sign Up", command=signUpBtn, height=50, width=100)
signUp_button.place(rely = 0.65, relx=0.5, anchor="center")

register_error=CTkLabel(master=register_frame, width=1000, height=100, text="", font=("aerial", 50), text_color="red")
register_error.place(anchor="center", relx=0.5, rely=0.72)


#FORGOT PASSWORD
forgot_frame = CTkFrame(master=root)

forgot_to_login_button = CTkButton(master=forgot_frame, text="\u2190", width=10, height=50, corner_radius=100, command=forgotToLogin)
forgot_to_login_button.place(rely = 0.05, relx=0.05, anchor="center")

registerHeading=CTkLabel(master=forgot_frame, width=1000, height=100, text="Enter Credentials", font=("aerial", 72), text_color="white")
registerHeading.place(anchor="center", relx=0.5, rely=0.2)

forgot_username_entry = CTkEntry(master=forgot_frame, width=500, height=50, placeholder_text="Username")
forgot_username_entry.place(rely = 0.35, relx=0.5,anchor="center")

forgot_mobile_entry = CTkEntry(master=forgot_frame, width=500, height=50, placeholder_text="Mobile")
forgot_mobile_entry.place(rely = 0.4, relx=0.5,anchor="center")

forgot_email_entry = CTkEntry(master=forgot_frame, width=500, height=50, placeholder_text="Email")
forgot_email_entry.place(rely = 0.45, relx=0.5,anchor="center")

validate_button = CTkButton(master=forgot_frame, text="Validate", command=validateBtn)
validate_button.place(rely = 0.55, relx=0.5, anchor="center")

#CHANGE PASSWORD
change_frame = CTkFrame(master=root)

change_to_login_button = CTkButton(master=change_frame, text="\u2190", width=10, height=50, corner_radius=100, command=changeToLogin)
change_to_login_button.place(rely = 0.05, relx=0.05, anchor="center")

changeHeading=CTkLabel(master=change_frame, width=1000, height=100, text="Set New Password", font=("aerial", 72), text_color="white")
changeHeading.place(anchor="center", relx=0.5, rely=0.2)

change_password_entry = CTkEntry(master=change_frame, width=500, height=50, placeholder_text="New Password")
change_password_entry.place(rely = 0.4, relx=0.5,anchor="center")

change_button = CTkButton(master=change_frame, text="Change", command=changeBtn)
change_button.place(rely = 0.55, relx=0.5, anchor="center")

# HOME 
home_frame = CTkFrame(master=root)

home_to_login_button = CTkButton(master=home_frame, text="\u2190", width=10, height=50, corner_radius=100, command=homeToLogin)
home_to_login_button.place(rely = 0.05, relx=0.05, anchor="center")

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
createDatasetAudit()
createDatasetTrigger()
login_frame.pack(expand=True, fill=tk.BOTH)
root.mainloop()
# clearDataset()