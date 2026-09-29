import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import date, datetime

FONT = ("Times New Roman", 14)
FILE = "study_tasks.json"

class Task:
    def __init__(self, subject, topic, due_date, hours, done=False):
        self.subject = subject
        self.topic = topic
        self.due_date = due_date
        self.hours = hours
        self.done = done

    def to_text(self):
        status = "Done" if self.done else "Pending"
        return f"[{status}] {self.due_date} | {self.subject} | {self.topic} | {self.hours:g} hrs"

class StudyPlanner:
    def __init__(self):
        self.tasks = []
        if os.path.exists(FILE):
            try:
                with open(FILE) as f:
                    self.tasks = [Task(**t) for t in json.load(f)]
            except:
                self.tasks = []

    def save(self):
        with open(FILE, "w") as f:
            json.dump([t.__dict__ for t in self.tasks], f, indent=4)

    def add(self, task):
        self.tasks.append(task)
        self.tasks.sort(key=lambda t: t.due_date)
        self.save()

    def mark_done(self, i):
        self.tasks[i].done = True
        self.save()

    def delete(self, i):
        self.tasks.pop(i)
        self.save()

class PlannerApp:
    def __init__(self, root):
        self.planner = StudyPlanner()
        root.title("Study Planner")
        root.geometry("750x850")

        tk.Label(root, text="Study Planner", font=("Times New Roman", 17, "bold")).pack(pady=10)
        self.entries = []
        for name in ["Subject:", "Topic:", "Due Date (YYYY-MM-DD):", "Study Hours:"]:
            tk.Label(root, text=name, font=FONT).pack()
            e = tk.Entry(root, font=FONT)
            e.pack(pady=5)
            self.entries.append(e)

        tk.Button(root, text="Add Task", command=self.add_task, bg="light blue", font=FONT).pack(pady=15)
        tk.Label(root, text="Study Tasks:", font=FONT).pack()
        self.task_list = tk.Listbox(root, width=60, height=12, font=FONT)
        self.task_list.pack(pady=10)

        frame = tk.Frame(root)
        frame.pack(pady=5)
        tk.Button(frame, text="Mark as Done", command=self.mark_done, bg="light green", font=FONT).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Delete Selected", command=self.delete_task, bg="salmon", font=FONT).pack(side=tk.LEFT, padx=10)

        self.progress = tk.Label(root, font=("Times New Roman", 15, "bold"))
        self.progress.pack(pady=10)
        self.refresh()

    def add_task(self):
        subject, topic, due, hours = [e.get().strip() for e in self.entries]

        if subject == "" or topic == "":
            messagebox.showwarning("Input Error", "Please Enter Both A Subject And A Topic")
            return
        try:
            d = datetime.strptime(due, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showwarning("Wrong Date Entered", "Please Enter The Date as YYYY-MM-DD")
            return
        if d < date.today():
            messagebox.showwarning("Input Error", "Due Date Can't Be In The Past")
            return
        try:
            hours = float(hours)
        except ValueError:
            messagebox.showwarning("Wrong Hours Entered", "Please Enter The Study Hours As A Number")
            return
        if hours <= 0:
            messagebox.showwarning("Input Error", "Study Hours Must Be Greater Than Zero")
            return

        self.planner.add(Task(subject, topic, due, hours))
        self.refresh()
        for e in self.entries:
            e.delete(0, tk.END)

    def mark_done(self):
        if not self.task_list.curselection():
            messagebox.showwarning("Selection Error", "Please Select A Task To Mark As Done")
            return
        self.planner.mark_done(self.task_list.curselection()[0])
        self.refresh()

    def delete_task(self):
        if not self.task_list.curselection():
            messagebox.showwarning("Selection Error", "Please Select A Task To Delete")
            return
        self.planner.delete(self.task_list.curselection()[0])
        self.refresh()

    def refresh(self):
        self.task_list.delete(0, tk.END)
        for t in self.planner.tasks:
            self.task_list.insert(tk.END, t.to_text())
            if t.done:
                self.task_list.itemconfig(tk.END, fg="green")

        done = sum(1 for t in self.planner.tasks if t.done)
        left = sum(t.hours for t in self.planner.tasks if not t.done)
        self.progress.config(text=f"Completed: {done} / {len(self.planner.tasks)}   |   Hours Left: {left:g}")


root = tk.Tk()
PlannerApp(root)
root.mainloop()