# 🏦 Loan Eligibility Predictor

A smart, interactive desktop application that predicts loan eligibility using a trained machine learning model. Built with 💡 machine learning, 🎨 Tkinter UI, and 🔍 real-time feedback—all wrapped in a clean, user-friendly experience.

![screenshot](illustration.png)

---

## 🚀 Features

- ✅ Predicts loan approval based on applicant details
- 📊 Displays confidence score for every prediction
- 🎨 Stylish UI with color-coded results (green for approval, red for rejection)
- 🧠 Intelligent rejection reasons (e.g. low credit history, insufficient income)
- 💾 Trained on real-world loan data using Random Forest classifier

---

## 🛠 Tech Stack

| Layer         | Tools Used                     |
|---------------|--------------------------------|
| UI            | Tkinter + PIL (for images)     |
| ML Model      | Scikit-learn (Random Forest)   |
| Data Handling | Pandas, NumPy                  |
| Packaging     | joblib                         |

---

## 📂 Project Structure

```plaintext
Loan-Eligibility-Predictor/
├── src/                 # Source code files
├── data/                # Dataset files (if included)
├── model/               # Trained machine learning model (.joblib)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── illustration.png     # UI screenshot
└── main.py              # Main application file
```

---

## 💻 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/YourUsername/Loan-Eligibility-Predictor.git
cd Loan-Eligibility-Predictor
```

2. **Install required libraries**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

---

## 🎥 Demo

*(Optional: Add your demo video link here if you have one)*

---

## 🔮 Future Improvements

- Deploy as a web application using Streamlit
- Improve model accuracy with more features
- Add user authentication for sensitive predictions

---

## 📞 Contact

*Developed by [Your Name](https://github.com/YourUsername)*  
Email: your.email@example.com
