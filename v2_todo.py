# Main Programme

import v2_todo_utils as td

tasks = []

def condition_1(tasks):
    

    task = td.bs.input_specific_int("\nEnter Task", 0, 1)

    if task == 0:
        return
    
    td.add_task(tasks)
    return 

def condition_2(tasks):

    task = td.bs.input_specific_int("Enter Task", 0, 3)

    match task:
        case 0:
            td.bs.center("Programme Stopped", 40, "=", "\n")
        case 1:
            td.add_task(tasks)
        case 2:
            td.display_tasks(tasks)
        case 3:
            td.remove_task(tasks)
    
def condition_check(tasks):

    if len(tasks) == 0:
        return 1
    else:
        return 2

def to_do(tasks):
    td.bs.center("To-Do App (terminal based)", 60, "=", "\n")

    while True:
        condition = condition_check(tasks)

        match condition:
            case 1:

                td.bs.table_formatting(2, 40, "To-Do App (Terminal Based)", td.bs.table_data(["Code", "Function"], [[0,1], ["Stop The program", "Add Tasks"]]))
                condition_1(tasks)
            case 2:

                td.bs.table_formatting(2, 40, "To-Do App (Terminal Based)", td.bs.table_data(["Code", "Function"], [[0,1, 2, 3], ["Stop The program", "Add Tasks", "Display Tasks", "Remove Tasks"]]))
                condition_2(tasks)

to_do(tasks)