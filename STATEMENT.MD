## 📌Problem Statement
Many students find it hard to manage their study time, especially when several subjects, assignments and exams come up at once.
Without a simple plan, topics are left to the last minute, deadlines are missed and it is difficult to see how much work is still left.
Many existing planner apps need online accounts, have too many features, or show adverts, which is more than a student needs to plan a few weeks of study.

## 📌Scope of the Project
This project aims to develop a Study Planner, a client-side desktop application.
It bridges the gap between writing plans on paper and using heavy online productivity tools.

The scope includes:
* Local Data Storage: Using a local JSON file to save study tasks without requiring internet access or external accounts.
* Data Processing: Logic to validate input, sort tasks by due date, mark tasks as done, and calculate completed tasks and hours left.
* Object-Oriented Structure: The program is split into three classes (Task, StudyPlanner, PlannerApp) that separate the data, the storage logic and the user interface.
* Resilience: The application handles a missing or empty data file gracefully and rejects invalid input before it is saved.

## 📌Target Users
* School and College Students: Users who want to plan study sessions for different subjects before tests and exams.
* Competitive Exam Aspirants: Students who need to divide a large syllabus into topics with target dates.
* Self Learners: People learning a new skill who want to track topics and hours.
* General Users: Anyone who wants a simple offline to-do list with deadlines and time estimates.

## 📌High-Level Features
* Task Planning: Add study tasks with subject, topic, due date and study hours.
* Smart Input Validation: Refuses blank fields, badly formatted or past dates, and hours that are not positive numbers, preventing bad data and crashes.
* Automatic Sorting: Tasks are always listed in order of due date.
* Progress Tracking: Shows completed tasks out of the total and the study hours still left.
* Persistent Local Storage: Tasks are saved automatically to a JSON file and reloaded the next time the app is launched.
* Simple GUI: A clean Tkinter interface with Times New Roman styling where inputs, controls and results are clearly separated.
