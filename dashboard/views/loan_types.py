import tkinter as tk

def show_loan_types(main_area):
    for widget in main_area.winfo_children():
        widget.destroy()

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
        text="🏦 Types of Loans",
        font=("Helvetica", 20, "bold"),
        bg="white",
        fg="#2c3e50"
    ).pack(anchor="w", pady=(10, 20))

    # Loan categories
    loan_info = [
        ("Home Loan", 
         "Used to purchase, construct, or renovate residential property. Usually long-term with lower interest rates."),
        
        ("Personal Loan", 
         "Unsecured loan for personal needs like travel, marriage, or medical emergencies. Quick, but carries higher interest."),

        ("Education Loan", 
         "Designed to cover tuition, books, and living expenses for students pursuing higher studies. Often offers grace periods."),

        ("Business Loan", 
         "Helps entrepreneurs fund new ventures or expand operations. Can be secured or unsecured, with custom repayment terms."),

        ("Vehicle Loan", 
         "Used to purchase cars or two-wheelers. The vehicle usually serves as collateral."),

        ("Gold Loan", 
         "Loan provided against gold ornaments. Instant disbursement with relatively lower documentation."),
    ]

    for title, desc in loan_info:
        tk.Label(scroll_frame, text=title, font=("Helvetica", 15, "bold"), bg="white").pack(anchor="w", pady=(10, 5))
        tk.Label(scroll_frame, text=desc, font=("Helvetica", 12), wraplength=800, justify="left", bg="white").pack(anchor="w", pady=(0, 10))