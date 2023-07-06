import tkinter as tk
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="YOURSERVERIP",
    user="david",
    password="weakpassword",
    database="dumbdb"
)
cursor = db.cursor()

def update_top_users():
    # Fetch the top eight users with the highest WPM
    query = "SELECT id, nickname, word_per_minute, `date`, `time` FROM typing_results WHERE accuracy >= 75 ORDER BY word_per_minute DESC LIMIT 8"
    cursor.execute(query)
    top_users = cursor.fetchall()

    # Clear the previous user labels in the frame
    for label in user_frame.winfo_children():
        label.destroy()

    # Create labels for each user and position them in a grid layout
    rankings = ["1등", "2등", "3등", "4등", "5등", "6등", "7등", "8등"]
    for i, user in enumerate(top_users):
        row = i // 2  # Calculate the row index
        column = i % 2  # Calculate the column index

        user_label = tk.Label(
            user_frame,
            text=f"{rankings[i]}\n닉네임: {user[1]} \nID: {user[0]} \nWPM: {user[2]}\n날짜: {user[3]}\n시간: {user[4]}",
            font=("NoteSans", 30),
            borderwidth=2,
            relief="groove",
            padx=10,
            pady=10,
            bg="white",
            fg="black"
        )
        user_label.grid(row=row, column=column, padx=10, pady=10)

    db.commit()  # Commit the changes to the database

def update_leaderboard():
    update_top_users()
    window.after(20000, update_leaderboard)


window = tk.Tk()
window.title("WPM 리더보드")
window.geometry("800x600")

canvas = tk.Canvas(window, bg="white")
canvas.pack(fill="both", expand=True)

#title_label = tk.Label(canvas, text="리더보드 - WPM", font=("Arial", 4, "bold"), bg="white", fg="gold2")
#title_label2 = tk.Label(canvas, text="조건 : 정확도 75 이상", font=("Arial", 4, "bold"), bg="white", fg="DodgerBlue2")
#title_label.pack(pady=20)
#title_label2.pack(pady=5)

user_frame = tk.Frame(canvas, bg="white")
user_frame.pack(pady=10)
window.attributes('-fullscreen',True)

update_top_users()
update_leaderboard()

window.mainloop()

db.close()
