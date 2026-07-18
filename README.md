<h1 align="center">📧 Phishing Email Analyzer</h1>

<p align="center">
A Python & Flask based web application that analyzes email content to identify phishing indicators such as suspicious keywords and malicious links, then calculates a phishing risk score.
</p>

<p align="center">

<a href="https://python.org">
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
</a>

<a href="https://flask.palletsprojects.com/">
<img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask">
</a>

<a href="https://phishing-email-analyzer-5lbf.onrender.com">
<img src="https://img.shields.io/badge/🌐_Live_Demo-Visit-success?style=for-the-badge">
</a>

<a href="LICENSE">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</a>

</p>

---

# 📌 Overview

Phishing Email Analyzer is a Flask-based cybersecurity tool that analyzes email content for common phishing indicators. It detects suspicious keywords, identifies embedded URLs, calculates a phishing risk score, and classifies emails into different risk levels.

---

# ✨ Features

- ✅ Suspicious Keyword Detection
- ✅ URL Detection
- ✅ Phishing Risk Score Calculation
- ✅ Low / Medium / High Risk Classification
- ✅ Clean & Responsive User Interface
- ✅ Built with Python & Flask

---

# 📸 Screenshots

### 🏠 Home Page

![Home](screenshots/home.png)

### 🔍 Analysis Result

![Result](screenshots/result.png)

---

# 🛠️ Tech Stack

- Python
- Flask
- HTML5
- CSS3
- Regular Expressions (Regex)

---

# 📂 Project Structure

```text
Phishing-Email-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── screenshots/
│   ├── home.png
│   └── result.png
├── templates/
│   └── phishing.html
└── static/
    └── style.css
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/SyedTaif/Phishing-Email-Analyzer.git
```

### Navigate to the project directory

```bash
cd Phishing-Email-Analyzer
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

### Open in your browser

```text
http://127.0.0.1:5000
```

---

# 🚀 Live Demo

🌐 https://phishing-email-analyzer-5lbf.onrender.com

---

# 🔍 Detection Logic

The application analyzes email content using:

- Suspicious keyword matching
- URL extraction using Regular Expressions (Regex)
- Risk score calculation
- Risk classification (Low / Medium / High)

---

# 🔮 Future Improvements

- Sender Email Verification
- Domain Reputation Check
- Attachment Analysis
- Machine Learning Detection
- Email Header Analysis
- VirusTotal API Integration

---

# 👨‍💻 Author

**Syed Taif Ahmed**

🌐 GitHub: https://github.com/SyedTaif

💼 LinkedIn: https://www.linkedin.com/in/syed-taif-ahmed-ba8a683bb/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
