'''
Title: Group GUI task
Author: Forest
Date: 2024/05/16
Program description: Group GUI Task, including Username, Password, Loggin, Register and Language select.
'''

import tkinter as tk
from tkinter import messagebox
import data

# 不同語言顯示之文本
languages = {
    "繁體中文": {"username": "用戶名", "password": "密碼", "login": "登入", "register": "注冊",
                 "login_success_title": "登入成功", "login_success_content": "歡迎，",
                 "login_failure": "用戶名或密碼錯誤", "register_success": "注冊成功",
                 "register_failure": "用戶名已存在", "language": "選擇語言"},
    "简体中文": {"username": "用户名", "password": "密码", "login": "登录", "register": "注册",
                 "login_success_title": "登录成功", "login_success_content": "欢迎，",
                 "login_failure": "用户名或密码错误", "register_success": "注册成功",
                 "register_failure": "用户名已存在", "language": "选择语言"},
    "English": {"username": "Username", "password": "Password", "login": "Login", "register": "Register",
                "login_success_title": "Login Successful", "login_success_content": "Welcome, ",
                "login_failure": "Invalid username or password", "register_success": "Registration Successful",
                "register_failure": "Username already exists", "language": "Language"},
    "Deutsch": {"username": "Benutzername", "password": "Passwort", "login": "Anmelden", "register": "Registrieren",
                "login_success_title": "Erfolgreich angemeldet", "login_success_content": "Willkommen, ",
                "login_failure": "Benutzername oder Passwort ist falsch",
                "register_success": "Registrierung erfolgreich", "register_failure": "Benutzername existiert bereits",
                "language": "Sprache"},
    "Norsk": {"username": "Brukernavn", "password": "Passord", "login": "Logg inn", "register": "Registrer",
              "login_success_title": "Innlogging vellykket", "login_success_content": "Velkommen, ",
              "login_failure": "Ugyldig brukernavn eller passord", "register_success": "Registrering vellykket",
              "register_failure": "Brukernavn finnes allerede", "language": "Språk"}
}

current_language = "繁體中文"


def set_language(lang):
    global current_language
    current_language = lang
    label_username.config(text=languages[lang]["username"])
    label_password.config(text=languages[lang]["password"])
    label_language.config(text=languages[lang]["language"])
    button_login.config(text=languages[lang]["login"])
    button_register.config(text=languages[lang]["register"])


# 登入功能
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in data.user_data and data.user_data[username] == password:
        messagebox.showinfo(languages[current_language]["login_success_title"],
                            f"{languages[current_language]['login_success_content']}{username}!")
    else:
        messagebox.showerror(languages[current_language]["login_failure"], languages[current_language]["login_failure"])


# 注冊功能
def register():
    username = entry_username.get()
    password = entry_password.get()

    if username in data.user_data:
        messagebox.showerror(languages[current_language]["register_failure"],
                             languages[current_language]["register_failure"])
    else:
        data.user_data[username] = password
        with open('data.py', 'w') as file:
            file.write(f"user_data = {data.user_data}")
        messagebox.showinfo(languages[current_language]["register_success"],
                            f"{languages[current_language]['register_success']}, {username}!")


# 創建主窗口
root = tk.Tk()
root.title("Login")

# 語言選擇下拉菜單
frame_language = tk.Frame(root)
frame_language.pack()

label_language = tk.Label(frame_language, text=languages[current_language]["language"])
label_language.pack(side=tk.LEFT)

language_var = tk.StringVar(root)
language_var.set(current_language)

language_menu = tk.OptionMenu(frame_language, language_var, *languages.keys(), command=set_language)
language_menu.pack(side=tk.LEFT)

# 用戶名標簽和輸入框
label_username = tk.Label(root, text=languages[current_language]["username"])
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

# 密碼標簽和輸入框
label_password = tk.Label(root, text=languages[current_language]["password"])
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

# 登入和注冊按鈕框架
frame_buttons = tk.Frame(root)
frame_buttons.pack()

# 登入按鈕
button_login = tk.Button(frame_buttons, text=languages[current_language]["login"], command=login)
button_login.pack(side=tk.LEFT)

# 注冊按鈕
button_register = tk.Button(frame_buttons, text=languages[current_language]["register"], command=register)
button_register.pack(side=tk.LEFT)

# 進入主循環
root.mainloop()
