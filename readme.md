# 🧠 TaskMind AI Agent

TaskMind AI Agent is a **Python-based smart productivity assistant** built with **Tkinter GUI** and powered by **Google Gemini AI (gemini-1.5-flash)**.

It helps users manage daily tasks by automatically:

* Classifying tasks
* Assigning priorities
* Providing productivity suggestions

---

## 🚀 Features

* ✅ Simple and interactive GUI (Tkinter)
* 🤖 AI-powered task classification
* 📊 Automatic priority assignment (High, Medium, Low)
* 💡 Smart productivity suggestions
* ✔ Mark tasks as completed
* 🗑 Delete tasks easily

---

## 🛠 Technologies Used

* Python
* Tkinter (GUI)
* Google Generative AI (Gemini API)

---

## ⚙️ How It Works

1. User enters their name
2. Adds a task
3. AI Agent:

   * Classifies task (Study / Work / Personal / General)
   * Assigns priority
   * Suggests improvement tip
4. Task gets added to the list with AI insights

---

## 📦 Installation & Setup

1. Install required library:

```bash
pip install google-generativeai
```

2. Add Gemini API key:

```python
genai.configure(api_key="my_personal_key")  
# note : I could not share my personal key 
```

3. Run the app:

```bash
python agent.py
```

---

## 📌 Example Output

Task: "Complete Python assignment"

Output:

* Category: Study
* Priority: High
* Suggestion: Break it into smaller steps for faster completion.

---

## 🌟 Future Improvements

* Voice-based interaction 🎤
* Task reminders ⏰
* Data saving (database integration)
* AI-powered scheduling 📅

---

## 👩‍💻 Author

Developed by **Qurat Ul Aen**
AI Developer | Python Enthusiast 🚀

---

## 💡 Note

This project uses **Gemini AI model** which can:

* Think intelligently 🤔
* Analyze tasks
* Perform decision-based actions

---

✨ Build smart. Work smarter.
