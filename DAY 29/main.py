from tkinter import *
from tkinter import messagebox
import random
import string
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password = ''.join(random.choice(letters + numbers + symbols) for _ in range(12))
  
    password_entry.delete(0, END)  
    password_entry.insert(0, password)  

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    

    with open("passwords.txt", "a") as file:
        json.dump(new_data, file,indent=4)


    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo(title="Success", message="Password saved successfully!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Logo Image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="C:/coding-programming/100 Days of Code/DAY 29/logo.png")  # Update path as needed
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()
email_entry = Entry(width=53)
email_entry.grid(row=2, column=1,columnspan=2, sticky="w")
password_entry = Entry(width=25 )
password_entry.grid(row=3,column=1, sticky="w")

# Buttons
search_button = Button(text="Search",width=14)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width= 45, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()