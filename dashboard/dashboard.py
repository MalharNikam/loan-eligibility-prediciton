import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from views.info import show_info
from views.loan_types import show_loan_types
from views.accepted_loans import show_accepted_loans
from views.check_eligibility import show_check_eligibility





# Initialize window
root = tk.Tk()
root.title("Loan Eligibility Dashboard")
root.geometry("1300x750")
root.configure(bg="white")

# === Sidebar Frame (wider) ===
sidebar = tk.Frame(root, bg="#2c3e50", width=340)
sidebar.pack(side="left", fill="y")

# === Sidebar Buttons with Hover ===
def create_sidebar_button(parent, text, command=None):
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        font=("Helvetica", 14),
        bg="#34495e",
        fg="white",
        activebackground="#1abc9c",
        activeforeground="white",
        relief="flat",
        bd=0,
        padx=20,
        pady=14,
        anchor="w",
        cursor="hand2"
    )
    btn.pack(fill="x", pady=5)

    def on_enter(e): btn.config(bg="#1abc9c")
    def on_leave(e): btn.config(bg="#34495e")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# Add buttons to sidebar
create_sidebar_button(sidebar, "📋  Check Eligibility", lambda: show_check_eligibility(main_area))
create_sidebar_button(sidebar, "📈  Accepted Loans", lambda: show_accepted_loans(main_area))
create_sidebar_button(sidebar, "ℹ️  Information", lambda: show_info(main_area))
create_sidebar_button(sidebar, "🏦  Types of Loans", lambda: show_loan_types(main_area))

# === Main Content Area ===
main_area = tk.Frame(root, bg="white")
main_area.pack(side="right", fill="both", expand=True)


# Heading
header_font = font.Font(family="Helvetica", size=26, weight="bold")
tk.Label(
    main_area,
    text="📊 Loan Eligibility Prediction",
    font=header_font,
    bg="white",
    fg="#2c3e50"
).pack(pady=(0, 30))

# Background Image in a specific compartment
try:
    image = Image.open("bg.jpeg")  # <-- replace with your background illustration
    image = image.resize((580, 380))  # Adjust as needed
    image_tk = ImageTk.PhotoImage(image)

    image_frame = tk.Frame(main_area, bg="white", width=600, height=400)
    image_frame.pack(pady=10)
    tk.Label(image_frame, image=image_tk, bg="white").pack()
except:
    tk.Label(main_area, text="[Background image not found]", font=("Helvetica", 12), bg="white", fg="red").pack()

root.mainloop()