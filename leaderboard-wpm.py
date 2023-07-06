import tkinter as tk
import mysql.connector
from colorama import init, Fore, Style

# Connect to the MySQL database
db = mysql.connector.connect(
    host="YOURSERVERIP",
    user="david",
    password="weakpassword",
    database="dumbdb"
)
cursor = db.cursor()

def update_top_users():
    # Fetch the top three users with the highest WPM
    query = "SELECT id, nickname, word_per_minute, `date`, `time` FROM typing_results WHERE accuracy >= 75 ORDER BY word_per_minute DESC LIMIT 3"
    cursor.execute(query)
    top_users = cursor.fetchall()

    # Clear the previous user labels
    for label in user_labels:
        label.destroy()

    # Create labels for each user
    for i, user in enumerate(top_users):
        user_label = tk.Label(
            canvas,
            text=f"닉네임: {user[1]} \nID: {user[0]} \nWPM: {user[2]}\n날짜: {user[3]}\n시간: {user[4]}",
            font=("NoteSans", 32),
            borderwidth=2,
            relief="groove",
            padx=10,
            pady=10,
            bg="white",
            fg="black"
        )
        user_label.pack()
        user_labels.append(user_label)
window = tk.Tk()
window.title("WPM 리더보드")
window.geometry("800x600")

canvas = tk.Canvas(window, bg="white")
canvas.pack(fill="both", expand=True)
title_label = tk.Label(canvas, text="리더보드 - WPM", font=("Arial", 40, "bold"), bg="white", fg="gold2")
title_label2 = tk.Label(canvas, text="조건 : 정확도75이상", font=("Arial", 25, "bold"), bg="white", fg="DodgerBlue2")

title_label.pack(pady=20)
title_label2.pack(pady=5)
user_labels = []
update_top_users()
window.after(5000, update_top_users)
window.mainloop()
db.close()