import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import subprocess
import sys
import os

root = tk.Tk()
root.title("Loan Predictor - Welcome")
root.geometry("900x500")
root.configure(bg="white")

# Load image
img = Image.open("background.png")  # Make sure this exists in your root directory
img = img.resize((300, 300))
img_tk = ImageTk.PhotoImage(img)

# Layout
left = tk.Frame(root, bg="white")
left.pack(side="left", fill="both", expand=True)

right = tk.Frame(root, bg="white")
right.pack(side="right", fill="both", expand=True)

# Greeting
fancy_font = font.Font(family="Segoe Script", size=18, weight="bold")
greeting = (
    "👋 Hello, welcome to\n"
    "Loan Eligibility Predictor\n\n"
    "Want to check if you're eligible or not?"
)

tk.Label(
    left,
    text=greeting,
    font=fancy_font,
    bg="white",
    fg="black",
    justify="left",
    wraplength=380
).pack(pady=80)

# Launch dashboard
def open_dashboard():
    dashboard_path = os.path.join("dashboard", "dashboard.py")
    subprocess.Popen([sys.executable, dashboard_path])

# Launch Button
tk.Button(
    root,
    text="✅ Check Now",
    command=open_dashboard,
    font=("Helvetica", 13, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10
).pack(side="bottom", pady=30)

# Image display
tk.Label(right, image=img_tk, bg="white").pack(pady=60)

root.mainloop()