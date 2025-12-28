import tkinter as tk
root = tk.Tk()

task = []

def toggle_task(task_info):
    task_label = task_info['label']

    if task_info['done']:
        task_label.config(fg = "white", font = ("TkDefaultFont", 12, "normal"))
        task_info['done'] = False
    else:
        task_label.config(fg = "grey", font = ("TkDefaultFont", 12, "overstrike"))
        task_info['done'] = True 
    return       

def add_task( e = None):
    task_grab = enter.get().strip()
    if task_grab == "":
        return

    task_label = tk. Label(tsk, text = task_grab, anchor='w')
    task_label. pack(fill='x', pady=2)
    task_info = {'label': task_label, 'done': False}
    task_label.bind("<Button-1>", lambda e: toggle_task(task_info))

    enter.delete(0, tk.END)
    enter.focus_set()
    return

root.title("Task manager")
root.geometry("500x300+200+200")

inpt = tk.Frame(root)
tsk = tk.Frame(root)

inpt.pack()
tsk.pack(padx = 10, fill = "x")

enter = tk.Entry(inpt, width = 35)
add = tk.Button(inpt, text = "Add task", command = add_task)
enter.focus()

enter.grid(row = 0, column = 0)
add.grid(row = 0, column = 1, padx = 5)

enter.bind("<Return>", add_task)

root.mainloop()