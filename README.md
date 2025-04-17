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
