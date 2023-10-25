from tkinter import*

def create_task(event):
    task = entry.get()
    if task:
        todo_list.insert(END, task)
        entry.delete(0, END)

def move_task(event,souerce_list,target_list):
    task = souerce_list.get(souerce_list.curselection())
    souerce_list.delete(souerce_list.curselection())
    target_list.insert(END,task)

def delete_all_task(event):

    todo_list.delete(0,END)
    in_progres_list.delete(0,END)
    done_list.delete(0,END)


root = Tk()
root.title('Kanban-Ban')
todo_list = Listbox(root, height = 10, width = 30)
in_progres_list = Listbox(root, height = 10, width = 30)
done_list = Listbox(root, height = 10, width = 30)


todo_list.grid(row=0, column=0, padx=10, pady=10)
in_progres_list.grid(row=0, column=1, padx=10, pady=10)
done_list.grid(row=0, column=2, padx=10, pady=10)


entry = Entry(root, width=30)
entry.grid(row = 1, column=1, pady=5)
add_buttom = Button(root, text='Add', width= 10)
add_buttom.grid(row=1, column=2, pady=5)
add_buttom.config(background='red')

clear_buttom = Button(root, text='Clear', width= 10)
clear_buttom.grid(row=4, column=1,pady=6)
add_buttom.bind("<Button-1>",create_task)
clear_buttom.bind("<Button-1>",delete_all_task)
root.config(background='yellow')
clear_buttom.config(background='blue')



todo_list.bind("<Double-Button-1>",lambda e:move_task(e, todo_list,in_progres_list))
in_progres_list.bind("<Double-Button-1>",lambda e:move_task(e,in_progres_list,done_list))
root.mainloop()
