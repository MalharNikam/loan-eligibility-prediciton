import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show_accepted_loans(main_area):
    for widget in main_area.winfo_children():
        widget.destroy()

    df = pd.read_csv("train.csv")
    accepted = df[df["Loan_Status"] == "Y"]

    # Canvas for scrollable visuals
    canvas = tk.Canvas(main_area, bg="white")
    scrollbar = tk.Scrollbar(main_area, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="white")

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
    scrollbar.pack(side="right", fill="y")

    # Total approved count
    total = accepted.shape[0]
    tk.Label(
        scroll_frame,
        text=f"✅ Total Approved Loans: {total}",
        font=("Helvetica", 16, "bold"),
        bg="white",
        fg="#27ae60"
    ).pack(anchor="w", pady=(10, 20))

    # Helper: attach a matplotlib figure to Tkinter
    def add_chart(fig):
        chart = FigureCanvasTkAgg(fig, master=scroll_frame)
        chart.draw()
        chart.get_tk_widget().pack(pady=20)

    # Chart 1: Approved Loans by Property Area + Education
    fig1, ax1 = plt.subplots(figsize=(6.5, 4))
    sns.countplot(data=accepted, x="Property_Area", hue="Education", palette="Set2", ax=ax1)
    ax1.set_title("Approved Loans by Area & Education")
    ax1.set_xlabel("Property Area")
    ax1.set_ylabel("Approved Count")
    plt.tight_layout()
    add_chart(fig1)

    # Chart 2: Pie Chart by Gender
    gender_counts = accepted["Gender"].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%", colors=["#66b3ff", "#ff9999"])
    ax2.set_title("Gender Split of Approved Loans")
    add_chart(fig2)

    # Chart 3: Stacked bar by Credit History + Property Area
    fig3, ax3 = plt.subplots(figsize=(6.5, 4))
    sns.countplot(data=accepted, x="Property_Area", hue="Credit_History", palette="coolwarm", ax=ax3)
    ax3.set_title("Approval by Area & Credit History")
    ax3.set_xlabel("Property Area")
    ax3.set_ylabel("Approved Count")
    plt.tight_layout()
    add_chart(fig3)