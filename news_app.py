import tkinter as tk
from tkinter import messagebox
import sqlite3
import requests
import io
from urllib.request import urlopen
from PIL import Image, ImageTk
import webbrowser
import pyttsx3

API_KEY = 'f64d0276546b4698b8d09359cc4be936'

BG_COLOR = '#add8e6'  # Light blue
FG_COLOR = 'black'

root = tk.Tk()
root.geometry('450x700')
root.resizable(0, 0)
root.title('NewsFeed App')
root.configure(bg=BG_COLOR)
engine = pyttsx3.init()

def create_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def login_screen():
    clear_screen()

    tk.Label(root, text="Login", font=("Verdana", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)

    tk.Label(root, text="Username", bg=BG_COLOR, fg=FG_COLOR).pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password", bg=BG_COLOR, fg=FG_COLOR).pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            load_news_app()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    tk.Button(root, text="Login", command=login, bg="gray20", fg="white").pack(pady=10)
    tk.Button(root, text="Register", command=register_screen, bg="gray30", fg="white").pack()

def register_screen():
    clear_screen()

    tk.Label(root, text="Register", font=("Verdana", 20), bg=BG_COLOR, fg=FG_COLOR).pack(pady=20)

    tk.Label(root, text="Username", bg=BG_COLOR, fg=FG_COLOR).pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password", bg=BG_COLOR, fg=FG_COLOR).pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def register():
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Fields cannot be empty")
            return

        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful")
            login_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")

    tk.Button(root, text="Register", command=register, bg="gray20", fg="white").pack(pady=10)
    tk.Button(root, text="Back to Login", command=login_screen, bg="gray30", fg="white").pack()

def load_news_app():
    try:
        response = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}')
        data = response.json()
        if response.status_code != 200 or data.get("status") != "ok":
            raise Exception(data.get("message", "Failed to fetch news"))
        load_news_item(data, 0)
    except Exception as e:
        clear_screen()
        tk.Label(root, text=f"Error: {e}", fg="red", bg=BG_COLOR, wraplength=300).pack(pady=20)

def speak_text(text):
    engine.stop() 
    engine.say(text)
    engine.runAndWait()

def load_news_item(data, index):
    clear_screen()
    try:
        img_url = data['articles'][index]['urlToImage']
        raw_data = urlopen(img_url).read()
        im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
        photo = ImageTk.PhotoImage(im)
    except:
        default_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
        raw_data = urlopen(default_url).read()
        im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
        photo = ImageTk.PhotoImage(im)

    label = tk.Label(root, image=photo, bg=BG_COLOR)
    label.photo = photo
    label.pack()

    title = data['articles'][index].get('title', 'No Title')
    desc = data['articles'][index].get('description', 'No Description')

    tk.Label(root, text=title, bg=BG_COLOR, fg=FG_COLOR, wraplength=350, justify='center', font=('verdana', 15)).pack(pady=(10, 20))
    tk.Label(root, text=desc, bg=BG_COLOR, fg=FG_COLOR, wraplength=350, justify='center', font=('verdana', 12)).pack(pady=(2, 20))

    speak_button = tk.Button(root, text="🔊 Speak", command=lambda: speak_text(f"{title}. {desc}"),
                             bg='gray30', fg='white', width=12, height=2)
    speak_button.pack(pady=(5, 15))

    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack()

    if index != 0:
        tk.Button(frame, text="Prev", width=12, height=2, command=lambda: load_news_item(data, index - 1),
                  bg='gray20', fg='white').pack(side='left')

    tk.Button(frame, text="Read More", width=12, height=2, command=lambda: webbrowser.open(data['articles'][index]['url']),
              bg='gray20', fg='white').pack(side='left')

    if index != len(data['articles']) - 1:
        tk.Button(frame, text="Next", width=12, height=2, command=lambda: load_news_item(data, index + 1),
                  bg='gray20', fg='white').pack(side='left')

    tk.Button(root, text="Logout", command=login_screen, bg="red", fg="white").pack(pady=10)

create_db()
login_screen()
root.mainloop()
