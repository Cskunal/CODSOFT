import tkinter as tk
from tkinter import messagebox

# This is the main window.
window = tk.Tk()
window.title("To-Do List")
window.geometry("400x500")
window.configure(bg = "#1E1128")

# We are storing our tasks in a list.
tasks = []

def add_tasks():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        tasks.append({"task": task, "done": False})
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Please enter your task.")

def delete_task():
    selected = listbox_tasks.curselection()
    if selected:
        index = selected[0]
        listbox_tasks.delete(index)
        del tasks[index]
    else:
        messagebox.showwarning("Please select a task.")

def mark_done():
    selected = listbox_tasks.curselection()
    if selected:
        index = selected[0]
        current_task = tasks[index]
        if not current_task["done"]:
            current_task["done"] = True
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, f"{current_task['task']}✅")
        else:
            messagebox.showinfo("Task is already completed.")
    else:
        messagebox.showwarning("Please select a task")

title = tk.Label(window, 
                 text = 'To-Do List', 
                 font = ("Ariel", 18, 'bold'),
                 bg = "#f0f0f0")
title.pack(pady = 10)

frame = tk.Frame(window)
frame.pack(pady=10)

entry_task = tk.Entry(frame,
                      width=30, 
                      font= ("Ariel", 12))
entry_task.pack(side = tk.LEFT, padx=(0, 10))

btn_add = tk.Button(frame, text = "Add Task", command = add_tasks,  bg="#4CAF50", fg="white")
btn_add.pack(side = tk.LEFT)

frame_listbox = tk.Frame(window)
frame_listbox.pack()

scrollbar = tk.Scrollbar(frame_listbox)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

listbox_tasks = tk.Listbox(frame_listbox,
                           height = 15,
                           width= 40,
                           font = ("Ariel", 12),\
                           yscrollcommand=scrollbar.set,
                           selectbackground="#a3d2ca"
                           )
listbox_tasks.pack()

scrollbar.config(command=listbox_tasks.yview)

btn_done = tk.Button(window, text = 'Marked Done', command=mark_done, bg = "#2196F3", fg="white", width=20)
btn_done.pack(pady= 5)

btn_delete = tk.Button(window, text = "Task Delete", command=delete_task,  bg="#f44336", fg="white", width=20)
btn_delete.pack(pady = 5)

window.mainloop()

