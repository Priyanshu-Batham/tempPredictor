import tkinter as tk
from tkinter import messagebox
from database import *
from machineLearning import *

#--------------------------UTILITY FUNCTIONS------------------------>>>>>>>>
#LOGIN FUNCTION
def loginBtn():
    username = username_entry.get()
    password = password_entry.get()

    if isUserPresent(username, password): #returns true or false
        welcome_label.config(text=f"Welcome {username}")

        login_frame.pack_forget() 
        home_frame.pack()        
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def registerBtn():
    login_frame.pack_forget()
    register_frame.pack()

def signUpBtn():
    username = register_username_entry.get()
    password = register_password_entry.get()
    mobile = register_mobile_entry.get()
    email = register_email_entry.get()

    createAccount(username, password, mobile, email)

    welcome_label.config(text=f"Welcome {username}")

    register_frame.pack_forget()
    home_frame.pack()

#FORGOT PASSWORD FUNCTION
def forgotPasswordBtn():
    login_frame.pack_forget()
    forgot_frame.pack()

#VALIDATE CREDENTIALS IF PASSWORD FORGOTTEN
def validateBtn():
    username = forgot_username_entry.get()
    mobile = forgot_mobile_entry.get()
    email = forgot_email_entry.get()

    if isCredentialsCorrect(username, mobile, email): #match the credentials
        forgot_frame.pack_forget()
        change_frame.pack()

    else:
        messagebox.showerror("Error", "Incorrect Credentials.")

#CHANGE PASSWORD
def changeBtn():
    username = forgot_username_entry.get()
    newPassword = change_password_entry.get()
    changePassword(username, newPassword)

    welcome_label.config(text=f"Welcome {username}")
    change_frame.pack_forget()
    home_frame.pack()

#PREDICT AND UPDATE THE OUTPUT TEXT
def predictBtn():
    response = predict()
    output_label.config(text=f"Tomorrow's temperature for Day{response[0]} is  {response[1]} \u00b0C")

# ---------------------------------FRAMES--------------------------------->>>>>>>>>
# MAIN 
root = tk.Tk()
root.geometry("600x400")
root.title("Login Page")

# LOGIN
login_frame = tk.Frame(root)

username_label = tk.Label(login_frame, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Login", command=loginBtn)
login_button.pack(pady=10)

register_button = tk.Button(login_frame, text="Register", command=registerBtn)
register_button.pack(pady=10)

forgot_button = tk.Button(login_frame, text="Forgot Password?", command=forgotPasswordBtn)
forgot_button.pack(pady=10)

#REGISTER 
register_frame = tk.Frame(root)

register_username_label = tk.Label(register_frame, text="Username: ")
register_username_label.grid(column = 0, row = 0, pady=10)
register_username_entry = tk.Entry(register_frame)
register_username_entry.grid(column = 1, row = 0, pady=5)

register_password_label = tk.Label(register_frame, text="Password:")
register_password_label.grid(column = 0, row = 1, pady=10)
register_password_entry = tk.Entry(register_frame)
register_password_entry.grid(column = 1, row = 1, pady=5)

register_mobile_label = tk.Label(register_frame, text="Mobile No: ")
register_mobile_label.grid(column = 0, row = 2, pady=10)
register_mobile_entry = tk.Entry(register_frame)
register_mobile_entry.grid(column = 1, row = 2, pady=5)

register_email_label = tk.Label(register_frame, text="Email: ")
register_email_label.grid(column = 0, row = 3, pady=10)
register_email_entry = tk.Entry(register_frame)
register_email_entry.grid(column = 1, row = 3, pady=5)

signUp_button = tk.Button(register_frame, text="Create Account", command=signUpBtn)
signUp_button.grid(column = 1, pady=10)

#FORGOT PASSWORD
forgot_frame = tk.Frame(root)

forgot_username_label = tk.Label(forgot_frame, text="Username: ")
forgot_username_label.grid(column = 0, row = 0, pady=10)
forgot_username_entry = tk.Entry(forgot_frame)
forgot_username_entry.grid(column = 1, row = 0, pady=5)

forgot_mobile_label = tk.Label(forgot_frame, text="Mobile No: ")
forgot_mobile_label.grid(column = 0, row = 1, pady=10)
forgot_mobile_entry = tk.Entry(forgot_frame)
forgot_mobile_entry.grid(column = 1, row = 1, pady=5)

forgot_email_label = tk.Label(forgot_frame, text="Email: ")
forgot_email_label.grid(column = 0, row = 2, pady=10)
forgot_email_entry = tk.Entry(forgot_frame)
forgot_email_entry.grid(column = 1, row = 2, pady=5)

validate_button = tk.Button(forgot_frame, text="Validate", command=validateBtn)
validate_button.grid(column = 1, pady=10)

#CHANGE PASSWORD
change_frame = tk.Frame(root)

change_password_label = tk.Label(change_frame, text="New Password: ")
change_password_label.grid(column = 0, row = 0, pady=10)
change_password_entry = tk.Entry(change_frame)
change_password_entry.grid(column = 1, row = 0, pady=5)

change_button = tk.Button(change_frame, text="Set Password", command=changeBtn)
change_button.grid(column = 1, row = 1, pady=10)

# HOME 
home_frame = tk.Frame(root)

welcome_label = tk.Label(home_frame, text="")
welcome_label.grid(row = 0, column = 0, columnspan=3, pady=20)

day_label = tk.Label(home_frame, text="Day")
day_label.grid(row = 1, column = 0, pady=5)

temp_label = tk.Label(home_frame, text="Temp")
temp_label.grid(row = 1, column = 2, pady=5)

day_entry = tk.Entry(home_frame)
day_entry.grid(row = 2, column = 0, pady=20)

temp_entry = tk.Entry(home_frame)
temp_entry.grid(row = 2, column = 2, pady=20)

add_button = tk.Button(home_frame, text="Add", command=lambda: addData(temp_entry.get()))
add_button.grid(row = 3, column = 0, pady=20)

update_button = tk.Button(home_frame, text="Update", command=lambda: updateData(day_entry.get(), temp_entry.get()))
update_button.grid(row = 3, column = 1, pady=20)

delete_button = tk.Button(home_frame, text="Delete", command=lambda: deleteData(day_entry.get()))
delete_button.grid(row = 3, column = 2, pady=20)

predict_button = tk.Button(home_frame, text="Predict", width=20, command=predictBtn)
predict_button.grid(row = 4, column = 0, columnspan=3, pady=5)

plot_button = tk.Button(home_frame, text="Plot Graph", width=20, command=plotDataFromDataset)
plot_button.grid(row = 5, column = 0, columnspan=3, pady=5)

output_label = tk.Label(home_frame, text="Temperature For Tomorrow")
output_label.grid(row = 6, column = 0, columnspan=3, pady=20)

#----------------------------INITIALIZING--------------------->>>>>>>>>>>>>
createTable()
createDataset()
login_frame.pack()
root.mainloop()