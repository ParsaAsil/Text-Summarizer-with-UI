# 🧠 Text Summarizer with UI

A Python-based GUI application that allows users to create accounts, log in, and summarize long texts using a pretrained NLP model. It features a clean Tkinter interface, dark/light mode switching, and support for multiple languages.

## 🎥 Demo

Watch how the app works:  
**▶️ [ApplicationVideo.mov](ApplicationVideo.mov)**

---

## 🚀 Features

- 🔐 Login & account creation with JSON-based storage
- 🧠 Extractive text summarization using `nltk`
- 🎨 Dark & Light mode support
- 🌍 Language switching (English, Persian, Indian)
- 🪄 Clean and responsive Tkinter UI

---

## 📁 Project Files

- `app.py` – Main application script
- `peopleData.txt` – Contains user data (first and last names in JSON format)
- `ApplicationVideo.mov` – Demo video showing how the app works
- `README.md` – Project documentation

---

## 📦 Installation

Before running the app, make sure you have Python 3 installed on your system.

### 1. Install Required Libraries

Use pip to install the main library:

pip install nltk

### 2. Install Tkinter (if not already installed)

Tkinter usually comes with Python, but if it’s missing, install it using:

•	macOS (with Homebrew):
  - brew install python-tk
    
•	Ubuntu / Debian:
  - sudo apt-get install python3-tk

### 3. Download NLTK Data

After installing NLTK, you need to download the required data.
Open a Python shell and run:

  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')

### 4. Run the Application

Once everything is installed, run the app using:
  python app.py

---

## 📝 peopleData.txt Format

```json
{
  "people": [
    {
      "first_name": "JOHN",
      "last_name": "DOE"
    },
    {
      "first_name": "JANE",
      "last_name": "SMITH"
    }
  ]
}
