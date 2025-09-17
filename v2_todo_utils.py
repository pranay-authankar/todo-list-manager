# add_task(task, tasks) → adds a task to the list.
# remove_task(task, tasks) → removes a task if it exists.
# show_tasks(tasks) → prints all tasks with numbers (1., 2., 3., …).
# clear_tasks(tasks) → removes all tasks.

import basic as bs

list_task = ["A", "f"]

def add_task(task_list):
    add = bs.input_all("Enter Task")

    if add not in task_list:
        task_list.append(add)
        print("\nTask Added\n")
    else:
        print("\nInfo : Task already in the To-Do List\n")
    
def remove_task(task_list):
    
    task = bs.input_specific_int("Enter task number", 1, len(task_list))
    task_list.pop(task-1)
    print("\nInfo : Task Removed")

def display_tasks(task_list):
    serial = []

    for i in range(len(task_list)):
        serial.append(i+1)

    tasks = []

    for task in task_list:
        tasks.append(task)

    bs.table_formatting(2, 20, "Your To-Do List", bs.table_data(["S.No", "Tasks"], [serial, tasks]))



display_tasks(list_task)
