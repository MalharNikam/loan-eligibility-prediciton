import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import joblib

model = joblib.load("loan_model.pkl")

def preprocess_inputs(values):
    mapping = {
        "Gender": {"Male": 1, "Female": 0},
        "Married": {"Yes": 1, "No": 0},
        "Dependents": {"0": 0, "1": 1, "2": 2, "3+": 3},
        "Education": {"Graduate": 0, "Not Graduate": 1},
        "Self_Employed": {"Yes": 1, "No": 0},
        "Property_Area": {"Urban": 0, "Rural": 1, "Semiurban": 2},
    }

    try:
        return [
            float(values["LoanAmount"]),
            mapping["Gender"][values["Gender"]],
            mapping["Married"][values["Married"]],
            mapping["Dependents"][values["Dependents"]],
            mapping["Education"][values["Education"]],
            mapping["Self_Employed"][values["Self_Employed"]],
            float(values["ApplicantIncome"]),
            float(values["CoapplicantIncome"]),
            int(values["Credit_History"]),
            mapping["Property_Area"][values["Property_Area"]],
        ]
    except Exception as e:
        raise ValueError(f"Input Error: {e}")

def show_check_eligibility(main_area):
    for widget in main_area.winfo_children():
        widget.destroy()

    master_frame = tk.Frame(main_area, bg="#f4f6f8")
    master_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(master_frame, bg="white", highlightthickness=0)
    scrollbar = tk.Scrollbar(master_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    scrollable_frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    image_frame = tk.Frame(master_frame, bg="#f4f6f8", width=400)
    image_frame.pack(side="right", fill="y")
    image_frame.pack_propagate(False)

    try:
        img_path = "illustration.png"
        if os.path.exists(img_path):
            img = Image.open(img_path).resize((600, 480))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(image_frame, image=photo, bg="#f4f6f8")
            img_label.image = photo
            img_label.pack(pady=100)
        else:
            raise FileNotFoundError(f"{img_path} not found")
    except Exception as e:
        print("Image error:", e)
        tk.Label(image_frame, text="📷 illustration.png not found", font=("Segoe UI", 12), fg="#888", bg="#f4f6f8").pack(pady=120)

    tk.Label(scrollable_frame, text="Loan Eligibility Form", font=("Segoe UI", 20, "bold"), bg="white").pack(anchor="w", pady=(30, 10), padx=40)

    form = tk.Frame(scrollable_frame, bg="white")
    form.pack(fill="x", padx=40)
    form.columnconfigure(0, weight=1, minsize=400)

    global fields
    fields = {}
    row = 0

    def section(title):
        nonlocal row
        tk.Label(form, text=title, font=("Segoe UI", 14, "bold"), bg="white").grid(row=row, column=0, sticky="w", pady=(25, 5))
        row += 1

    def field(label, widget):
        nonlocal row
        tk.Label(form, text=label, font=("Segoe UI", 12), bg="white").grid(row=row, column=0, sticky="w", pady=(10, 2))
        widget.grid(row=row + 1, column=0, sticky="ew", ipady=6, ipadx=6)
        row += 2

    def dropdown(var, options):
        opt = tk.OptionMenu(form, var, *options)
        opt.config(font=("Segoe UI", 12), width=30)
        return opt

    def entry():
        return tk.Entry(form, font=("Segoe UI", 12), bd=1, relief="solid")

    section("Business Details")
    fields["Loan_Type"] = tk.StringVar(value="Home Loan")
    field("Loan Type", dropdown(fields["Loan_Type"], ["Home Loan", "Personal Loan", "Education Loan", "Business Loan", "Vehicle Loan", "Gold Loan"]))
    fields["LoanAmount"] = entry()
    field("Loan Amount", fields["LoanAmount"])

    section("Personal Details")
    fields["Gender"] = tk.StringVar(value="Male")
    field("Gender", dropdown(fields["Gender"], ["Male", "Female"]))
    fields["Married"] = tk.StringVar(value="No")
    field("Married", dropdown(fields["Married"], ["Yes", "No"]))
    fields["Dependents"] = tk.StringVar(value="0")
    field("Dependents", dropdown(fields["Dependents"], ["0", "1", "2", "3+"]))
    fields["Education"] = tk.StringVar(value="Graduate")
    field("Education", dropdown(fields["Education"], ["Graduate", "Not Graduate"]))
    fields["Self_Employed"] = tk.StringVar(value="No")
    field("Self Employed", dropdown(fields["Self_Employed"], ["Yes", "No"]))
    fields["ApplicantIncome"] = entry()
    field("Applicant Income", fields["ApplicantIncome"])

    section("Co-Applicant Details")
    fields["CoapplicantIncome"] = entry()
    field("Coapplicant Income", fields["CoapplicantIncome"])
    fields["Credit_History"] = tk.StringVar(value="1")
    field("Credit History", dropdown(fields["Credit_History"], ["1", "0"]))
    fields["Property_Area"] = tk.StringVar(value="Urban")
    field("Property Area", dropdown(fields["Property_Area"], ["Urban", "Rural", "Semiurban"]))

    def run_prediction():
        try:
            values = {}
            for k, widget in fields.items():
                val = widget.get() if isinstance(widget, tk.StringVar) else widget.get()
                if val.strip() == "":
                    messagebox.showwarning("Missing Info", f"Please fill out: {k.replace('_', ' ')}")
                    return
                values[k] = val

            processed = preprocess_inputs(values)
            proba = model.predict_proba([processed])[0]
            pred = model.predict([processed])[0]
            confidence = round(max(proba) * 100, 1)

            if pred == 1:
                result = f"✅ Eligible for Loan\nConfidence: {confidence}%"
                color = "#2ecc71"
            else:
                if int(values["Credit_History"]) == 0:
                    reason = "Low credit history"
                elif float(values["ApplicantIncome"]) < 2500:
                    reason = "Insufficient applicant income"
                else:
                    reason = "Does not meet eligibility criteria"
                result = f"❌ Not Eligible: {reason}\nConfidence: {confidence}%"
                color = "#e74c3c"

            output_label.config(text=result, bg=color, fg="white")

        except Exception as e:
            output_label.config(text=f"⚠️ {e}", bg="#e67e22", fg="white")

    tk.Button(
        scrollable_frame,
        text="Check Eligibility",
        font=("Segoe UI", 12, "bold"),
        bg="#2ecc71",
        fg="white",
        activebackground="#27ae60",
        relief="flat",
        padx=50,
        pady=10,
        command=run_prediction
    ).pack(pady=(30, 5), anchor="e", padx=40)

    output_label = tk.Label(
        scrollable_frame,
        text="",
        font=("Segoe UI", 13, "bold"),
        bg="white",
        fg="white",
        width=40,
        height=3,
        anchor="center",
        justify="center"
    )
    output_label.pack(pady=(0, 30), anchor="e", padx=40)