import tkinter as tk
from tkinter import messagebox
import google.generativeai as genai

# gemini model 
# genai.configure(api_key="")        note that I could not share my personal key 
model = genai.GenerativeModel("gemini-1.5-flash")


# AI logic 
def classify_task(task):
    prompt = f"""
    You are a smart productivity AI agent.

    Task: {task}

    1. Classify into one category: Study, Work, Personal, General
    2. Assign priority: High, Medium, Low
    3. Give one short productivity suggestion

    Output format:
    Category: <category>
    Priority: <priority>
    Suggestion: <suggestion>
    """

    try:
        response = model.generate_content(prompt)
        text = response.text

        category = text.split("Category:")[1].split("\n")[0].strip()
        priority = text.split("Priority:")[1].split("\n")[0].strip()
        suggestion = text.split("Suggestion:")[1].strip()

    except:
        category = "General"
        priority = "Low"
        suggestion = "Stay productive!"

    return category, priority, suggestion

# main app 
def open_agent():
    username = name_entry.get()

    if username == "":
        messagebox.showwarning("Warning", "Enter your name!")
        return

    start_window.destroy()

    # Agent Window
    root = tk.Tk()
    root.title("TaskMind AI Agent")
    root.geometry("450x600")
    root.config(bg="#f7f0f6")

    # Title
    title = tk.Label(root, text=f"Welcome, {username}", font=("Arial", 16, "bold"), bg="#f0f2f7")
    title.pack(pady=10)

    # Task Input
    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    # Functions inside to access UI
    def add_task():
        task = entry.get()

        if task == "":
            messagebox.showwarning("Warning", "Enter a task!")
            return

        category, priority, suggestion = classify_task(task)

        task_text = f"{task} | {category} | {priority}"
        listbox.insert(tk.END, task_text)

        suggestion_label.config(text=f" {suggestion}")

        entry.delete(0, tk.END)

    def delete_task():
        try:
            selected = listbox.curselection()
            listbox.delete(selected)
        except:
            messagebox.showwarning("Warning", "Select a task!")

    def mark_done():
        try:
            selected = listbox.curselection()
            task = listbox.get(selected)
            listbox.delete(selected)
            listbox.insert(tk.END, f"✔ DONE: {task}")
        except:
            messagebox.showwarning("Warning", "Select a task!")

    # Buttons
    add_btn = tk.Button(root, text="Add Task", bg="#4CAF50", fg="white", command=add_task)
    add_btn.pack(pady=5)

    listbox = tk.Listbox(root, width=55, height=15)
    listbox.pack(pady=10)

    done_btn = tk.Button(root, text="Mark as Done", bg="#2196F3", fg="white", command=mark_done)
    done_btn.pack(pady=5)

    delete_btn = tk.Button(root, text="Delete Task", bg="#f44336", fg="white", command=delete_task)
    delete_btn.pack(pady=5)

    suggestion_label = tk.Label(root, text="Suggestion will appear here", wraplength=400, fg="blue", bg="#f0f4f7")
    suggestion_label.pack(pady=15)

    root.mainloop()


#  Start Screen 
start_window = tk.Tk()
start_window.title("Enter TaskMind AI Agent")
start_window.geometry("350x250")
start_window.config(bg="#f7f2f0")

title = tk.Label(start_window, text="TaskMind AI Agent", font=("Arial", 16, "bold"), bg="#f0f4f7")
title.pack(pady=20)

name_label = tk.Label(start_window, text="Enter Your Name:", bg="#f0f4f7")
name_label.pack()

name_entry = tk.Entry(start_window, width=25)
name_entry.pack(pady=10)

enter_btn = tk.Button(start_window, text="Enter Agent", bg="#4CAF50", fg="white", command=open_agent)
enter_btn.pack(pady=10)

start_window.mainloop()
