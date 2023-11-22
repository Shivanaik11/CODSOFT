import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def add():
    task_string = task_field.get()
    
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Please enter a task.')
    else:
        tasks.append(task_string)
        list_update()
        task_field.delete(0, 'end')





def delete():
    try:
        selected_index = task_listbox.curselection()
        if not selected_index:
            raise tk.TclError

        tasks.pop(selected_index[0])
        list_update()
    except tk.TclError:
        messagebox.showinfo('Error', 'Please select a task to delete.')


def update():
    try:
        selected_index = task_listbox.curselection()
        if not selected_index:
            raise tk.TclError

        new_task_string = task_field.get()
        if len(new_task_string) == 0:
            messagebox.showinfo('Error', 'Please enter a new task.')
        else:
            tasks[selected_index[0]] = new_task_string
            list_update()
            task_field.delete(0, 'end')
    except tk.TclError:
        messagebox.showinfo('Error', 'Please select a task to update.')


def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)


def delete_all():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        while tasks:
            tasks.pop()
        list_update()


def clear_list():
    task_listbox.delete(0, 'end')


def close():
    print(tasks)
    guiWindow.destroy()


if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#52F9FF")

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="#52F9FF")
    functions_frame = tk.Frame(guiWindow, bg="#52F9FF")
    listbox_frame = tk.Frame(guiWindow, bg="#52F9FF")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(header_frame, text="To-Do List", font=("Copperplate Gothic Bold", "30"),
                             background="#52F9FF", foreground="black")
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(functions_frame, text="Enter the Task:", font=("Consolas", "11", "bold"),
                           background="#52F9FF", foreground="black")
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(functions_frame, font=("Consolas", "12"), width=18, background="#FFF8DC", foreground="black")
    task_field.place(x=30, y=80)

    add_button = ttk.Button(functions_frame, text="Add", width=18, command=add)
    del_button = ttk.Button(functions_frame, text="Delete", width=18, command=delete)
    update_button = ttk.Button(functions_frame, text="Update Task", width=18, command=update)
    del_all_button = ttk.Button(functions_frame, text="Delete All", width=18, command=delete_all)
    exit_button = ttk.Button(functions_frame, text="Exit", width=30, command=close)

    add_button.place(x=30, y=120)
    update_button.place(x=30, y=200)
    del_button.place(x=30, y=160)
    del_all_button.place(x=30, y=240)
    exit_button.place(x=60, y=280)

    task_listbox = tk.Listbox(listbox_frame, width=26, height=13, selectmode='SINGLE', background="#FFFFFF",
                              foreground="#000000", selectbackground="red", selectforeground="#FFFFFF")
    task_listbox.place(x=10, y=20)

    list_update()

    guiWindow.mainloop()
