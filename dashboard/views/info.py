import tkinter as tk

def show_info(main_area):
    for widget in main_area.winfo_children():
        widget.destroy()

    # Create scrollable canvas
    canvas = tk.Canvas(main_area, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(main_area, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="white")

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, padx=30, pady=30)
    scrollbar.pack(side="right", fill="y")

    # Heading
    tk.Label(
        scroll_frame,
        text="ℹ️ Understanding Loans & Eligibility",
        font=("Helvetica", 20, "bold"),
        bg="white",
        fg="#2c3e50"
    ).pack(anchor="w", pady=(10, 20))

    # Informational content
    info_points = [
        ("What is a loan?",
         "A loan is borrowed money that must be repaid with interest. It's used for expenses like housing, education, or emergencies."),
        
        ("Key Eligibility Factors",
         "• Income Level\n• Credit Score\n• Employment Type\n• Existing Debts\n• Collateral Value (if any)"),
        
        ("Tips to Improve Your Chances",
         "✔️ Maintain a strong credit history\n✔️ Keep income stable\n✔️ Limit liabilities\n✔️ Avoid frequent loan applications"),
        
        ("Common Mistakes",
         "❌ Applying to many lenders at once\n❌ Hiding financial data\n❌ Ignoring loan terms"),
        
        ("Documents You'll Likely Need",
         "• Aadhaar / PAN\n• Salary Slip / Income Proof\n• Bank Statements\n• Property or Purpose Proof"),
    ]

    for title, desc in info_points:
        tk.Label(scroll_frame, text=title, font=("Helvetica", 15, "bold"), bg="white").pack(anchor="w", pady=(10, 5))
        tk.Label(scroll_frame, text=desc, font=("Helvetica", 12), wraplength=800, justify="left", bg="white").pack(anchor="w", pady=(0, 10))