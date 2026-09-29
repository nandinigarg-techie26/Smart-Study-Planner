# Study Planner - Introduction to Problem Solving and Programming Project

## 📌Overview
This is a Python based desktop application with a GUI for planning study time, designed to help students break their syllabus into small study tasks, set a due date and the hours needed for each, and track which ones are finished. The tool uses tkinter for the frontend and a local JSON file for backend storage, so all tasks are saved automatically and remain available across sessions without needing an internet connection.

## 📌Features
* Task Planning: Add study tasks with a subject, topic, due date and the number of study hours.
* Sorted List: Tasks are automatically arranged by due date so the nearest deadline is always at the top.
* Mark as Done: Mark a finished task as done; completed tasks turn green in the list.
* Progress Tracking: Shows how many tasks are completed out of the total and how many study hours are left.
* Persistent Storage: Automatically saves all tasks to a local JSON file so data isn't lost when the app closes.
* Input Validation: Rejects a blank subject or topic, a wrongly formatted or past date, and hours that are not a positive number.
* Delete Tasks: Remove tasks that are no longer needed.
* User-Friendly GUI: Clean interface using Times New Roman font with clearly labelled fields and coloured buttons.
* Object-Oriented Design: The code is organised into three small classes, each with one job.

## 📌Code Design (Classes)
| Class | What it does |
|---|---|
| `Task` | Stores the details of one study task (subject, topic, due date, hours, done) and turns it into a line of text for display. |
| `StudyPlanner` | Keeps the list of tasks and handles loading, saving, adding, marking as done and deleting. |
| `PlannerApp` | Builds the tkinter window, reads the user's input, validates it, calculates progress and updates the list on screen. |

Keeping the data (`Task`, `StudyPlanner`) separate from the window (`PlannerApp`) means each part can be understood and changed on its own.

## 📌Technologies/Tools Used
* Programming Language: Python 3.7
* GUI Framework: Tkinter
* Data Format: JSON (local file storage)
* Standard Library: os, datetime, json

## 📌Steps to Install & Run the Project
### 1. *Requirement:*
Make sure that Python is installed on your system. You can check this by running:
```bash
python --version
```
### 2. *Clone/Download the Repository:*
Download the project files to your local machine.

### 3. *Install Dependencies:*
This project only uses Python's standard library (Tkinter comes with Python), so no extra installation is required.
### 4. *▶️ Run the Application:*
Go to your project directory and run the script:
```bash
python Study_Planner.py
```

## 📌Instructions for Testing
Conduct the following tests to ensure that the application works as anticipated.

### 1. *Standard Entry Test:*
* Launch the app.
* Enter "Maths" as the subject, "Integration" as the topic, a future date such as "2026-10-05" and "3" as the study hours.
* Click "Add Task."
* Expected Output: The task appears in the list as "[Pending]" and the progress shows "Completed: 0 / 1 | Hours Left: 3".

### 2. *Input Validation Test:*
* Leave the subject or topic blank, type a date like "05/10/2026" or a past date, or type "two" or "0" as the hours.
* Click "Add Task."
* Expected Output: A warning pop-up such as "Please enter both a subject and a topic", "Please enter the date as YYYY-MM-DD", "Due date cannot be in the past", "Please enter the study hours as a number" or "Study hours must be greater than zero".

### 3. *Sorting Test:*
* Add a task with a later due date, then one with an earlier due date.
* Expected Output: The earlier task is shown above the later one.

### 4. *Mark as Done Test:*
* Select a task and click "Mark as Done."
* Expected Output: The task changes to "[Done]" in green, the completed count goes up and its hours are removed from "Hours Left".

### 5. *Persistence Test:*
* Add a few tasks, mark one as done and close the application.
* Reopen the application.
* Expected Output: All tasks are still listed with the same status, loaded automatically from study_tasks.json.

### 6. *Delete Task Test:*
* Select a task and click "Delete Selected."
* Expected Output: The task is removed and the progress updates accordingly.

## 📌Project Structure

study planner
├── Study_Planner.py
├── study_tasks.json   (created automatically on first run)
├── README.md
├── statement.md
├── Project report.pdf
└──screenrecording

## 📌Screenshots
1. Entering a study task

<img width="941" height="1020" alt="image" src="https://github.com/user-attachments/assets/2ef48710-e958-4b38-bc57-7684cfefb91d" />

2. Tasks added to the list, sorted by due date

<img width="947" height="1016" alt="image" src="https://github.com/user-attachments/assets/923ad2fa-dc06-4011-89ad-febd1e7ea535

3. Two tasks marked as done (shown in green) and the progress updated

<img width="938" height="1017" alt="image" src="https://github.com/user-attachments/assets/e3e7bfb8-a860-4aef-9980-a86b4bcfcc2b" />

4. Warning when the study hours are not a number

<img width="1106" height="1011" alt="image" src="https://github.com/user-attachments/assets/1b07c815-53ad-4d33-86d9-3faea1ba08d6" />