# 📧 Phishing Email Analyzer

A Flask-based Phishing Email Analyzer that identifies suspicious email content by detecting phishing keywords, embedded URLs, and calculating a phishing risk score.

---

## 📌 Overview

Phishing attacks are one of the most common cyber threats. This project helps users analyze suspicious emails by checking for commonly used phishing keywords and detecting embedded URLs to estimate the likelihood of a phishing attempt.

---

## ✨ Features

- ✅ Suspicious Keyword Detection
- ✅ Embedded URL Detection
- ✅ Phishing Risk Score Calculation
- ✅ Low / Medium / High Risk Classification
- ✅ Clean & Responsive User Interface
- ✅ Built using Python & Flask

---

## 📸 Screenshots

### 🏠 Home Page

![Home](screenshots/home.png)

---

### 🚨 Email Analysis Result

![Result](screenshots/result.png)

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML5
- CSS3
- Regular Expressions (Regex)

---

## 📂 Project Structure

```text
phishing-email-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── screenshots/
│     ├── home.png
│     └── result.png
│
├── templates/
│     └── phishing.html
│
└── static/
      └── style.css
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/SyedTaif/phishing-email-analyzer.git
```

Move into the project directory

```bash
cd phishing-email-analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 🔍 How It Works

The analyzer performs the following checks:

- Detects phishing-related keywords
- Detects embedded URLs
- Assigns a risk score
- Classifies emails as:
  - 🟢 Low Risk
  - 🟡 Medium Risk
  - 🔴 High Risk

---

## 📈 Sample Analysis

| Detected Items | Risk Score | Risk Level |
|---------------|-----------:|-----------|
| No Suspicious Content | 0–30 | 🟢 Low |
| Few Keywords | 31–70 | 🟡 Medium |
| Multiple Keywords + URL | 71–100 | 🔴 High |

---

## 🔮 Future Improvements

- Machine Learning Based Detection
- AI-Powered Email Classification
- Attachment Analysis
- Domain Reputation Check
- Sender Reputation Analysis
- Real-time Threat Intelligence Integration

---

## 👨‍💻 Author

**Syed Taif Ahmed**

GitHub: https://github.com/SyedTaif

LinkedIn: https://www.linkedin.com/in/syed-taif-ahmed-ba8a683bb/

Portfolio: https://portfolio-rho-topaz-x4owcm1yim.vercel.app/

---

⭐ If you found this project useful, consider giving it a star.
