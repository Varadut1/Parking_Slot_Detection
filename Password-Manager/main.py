from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
COLOR = 'papaya whip'
COLOR2 = 'old lace'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)
    password1 = "".join(password_list)
    password.delete(0, END)
    password.insert(0, password1)
    pyperclip.copy(text=password1)
    messagebox.showinfo(title='About password', message='Password generated and copied to clipboard')

# ---------------------------- SAVE PASSWORD ------------------------------- #


def ADD():

    permission=None
    print()
    data = {
        website.get():{
            'email': email.get(),
            'password': password.get()
        }

    }
    if len(email.get()) != 0 and len(website.get()) != 0 and len(password.get()) != 0:
        permission = messagebox.askokcancel(title=f'{website.get()}',message=f'Your details are\nWebsite: {website.get()}\nEmail: {email.get()}\nPassword: {password.get()}\nIs it ok to save these details?')

    else:
        messagebox.showerror(title=f'Opps', message='Please do not leave any of the fields empty!')

    if permission:
        try:
            with open('Passwords.json', 'r') as f:
                existing_data = json.load(f)
                existing_data.update(data)
                data=existing_data
        except:
            pass
        finally:
            with open('Passwords.json', 'w') as f:
                json.dump(data, f, indent=4)
        with open('passwords.csv', 'a+') as f:
            f.write(f'\n{website.get()}, {email.get()}, {password.get()}')
        website.delete(0, END)
        password.delete(0, END)

def Search():
    with open('Passwords.json', 'r') as f:
        existing_data = json.load(f)
    if len(website.get())==0:
        messagebox.showerror(title='Unfilled', message='In order to search you need to fill the website box.')
    else:
        try:
            web_info = existing_data[website.get()]
            mail = web_info['email']
            pas = web_info['password']
            messagebox.showinfo(title=f'Info for {website.get()}', message=f'Email: {mail}\nPassword: {pas}')
        except:
            messagebox.showinfo(title='oops', message=f'No website named {website.get()} is reserved in database')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.minsize(550, 400)
window.config(padx=20, pady=40, bg=COLOR)
canvas = Canvas(height=200, width=200, bg=COLOR, highlightthickness=0)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0, padx=30)

# Labels
website_label = Label(text='Website: ', font=(FONT_NAME, 10, "bold"), bg=COLOR)
website_label.grid(column=0, row=1)
email_label = Label(text='Email/ Username: ', font=(FONT_NAME, 10, "bold"), bg=COLOR)
email_label.grid(column=0, row=2)
password_label = Label(text='Password: ', font=(FONT_NAME, 10, "bold"), bg=COLOR)
password_label.grid(column=0, row=3, padx=0, pady=5)

# Entries
website = Entry(width=32)
website.grid(column=1, row=1, padx=0)
website.focus()
email = Entry(width=57)
email.grid(column=1, row=2, columnspan=2, padx=0, pady=5)
email.insert(0, 'varaduttarwar535@gmail.com')
password = Entry(width=32)
password.grid(column=1, row=3, padx=0)
pass_gen = Button(text='Generate Password', command=gen_pass, font=(FONT_NAME, 10), bg=COLOR2)
pass_gen.grid(column=2, row=3, columnspan=2)
add_but = Button(text='Add', width=50, command=ADD, font=(FONT_NAME, 10), bg=COLOR2)
add_but.grid(column=1, row=4, columnspan=4, padx=5, pady=5)
search = Button(text='Search', width=17 ,command=Search, font=(FONT_NAME, 10), bg=COLOR2)
search.grid(column=2, row=1, columnspan=1)
window.mainloop()
