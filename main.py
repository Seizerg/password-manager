import tkinter
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    for i in range(0, 4):
        password.append(random.choice(letters))
    for i in range(0, 4):
        password.append(random.choice(symbols))
    for i in range(0, 4):
        password.append(random.choice(numbers))
    random.shuffle(password)
    new_pass = ''.join(password)
    password_input.delete(0, "end")
    password_input.insert(0, new_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website_entry = website_input.get()

    email_entry = email_input.get()
    password_entry = password_input.get()
    if len(website_entry) == 0:
        messagebox.showinfo(title="Error", message="Hey ur website box is empty")
        return
    if len(password_entry) == 0:
        messagebox.showinfo(title="Error", message="Hey ur password box is empty")
        return

    isOk = messagebox.askokcancel(title=website_entry,
                                  message=f"These are the details entered: \nEmail: {email_entry} \nPassword: {password_entry}\nTo continue press OK")
    if isOk:
        website_input.focus()
        with open("data.txt", mode="a") as file:
            file.write(f"{website_entry} | {email_entry} | {password_entry}\n")
            website_input.delete(0, "end")
            password_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
pic = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = tkinter.Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_input = tkinter.Entry(width=35)
email_input.insert(0, "sahil@123")
email_input.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1)

generate_pass = tkinter.Button(text="Generate Password", command=pass_generate)
generate_pass.grid(row=3, column=2)
add_pass = tkinter.Button(text="Add", width=35, command=save_pass)
add_pass.grid(row=4, column=1, columnspan=2)

window.mainloop()
