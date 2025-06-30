def home_page():
    name = input("Enter you name : ").strip().lower().capitalize()
    print(f"\nWelcome {name}\nI'm your To-Do List Manager\n")
    print("\nWhat are seeking for ?\t[Enter serial number / alphabet of the task]")

def add_new_task(list1, list2):
    print("\nWhere do you want to add new task\n1. Pending Task\n2. Done Task\n")
    stop1 = False
    while stop1 == False:
        task_type = input("-> ")
        if task_type and task_type.isdigit():
            task_type = int(task_type)
            if task_type == 1:
                new_task = input("\nEnter the task\n-> ")
                list2.append(new_task)
                print("\n---Task Updated---")
                stop2 = False
                while stop2 == False:
                    inp = input("\nWant to add another task\n(y/n) : ")
                    if inp:
                        if inp == "y":
                            add_new_task(list1, list2)
                            stop = True
                            stop1 = True
                            stop2 = True
                        elif inp == "n":
                            print("\n---Updated Pending Tasks---")
                            i = 1
                            for x in list2:
                                print(f"{i}) {x}")
                                i += 1
                            stop = True
                            stop1 = True
                            stop2 = True
                        else:
                            print("\nEnter 'y' or 'n'")
                    else:
                        print("Seems like you didn't enter anything\nEnter value of 'y' or 'n'")
            elif task_type == 2:
                stop2 = False
                while stop2 == False:
                    new_task = input("\nEnter the task\n-> ")
                    if new_task:
                        list1.append(new_task)
                        print("\n---Task Updated---")
                        stop = False
                        while stop == False:
                            inp = input("\nWant to add another task\n(y/n) : ")
                            if inp:
                                if inp == "y":
                                    add_new_task(list1, list2)
                                    stop = True
                                    stop1 = True
                                    stop2 = True
                                elif inp == "n":
                                    stop = True
                                    stop1 = True
                                    stop2 = True
                                else:
                                    print("\nEnter 'y' or 'n'")
                            else:
                                print("Seems like you didn't enter anything\nEnter value of 'y' or 'n'")
                    else:
                        print("\nSeems like you didn't enter anything\nTry again")
            else:
                print("\n[Enter 1 or 2]")
        else:
            print("\nEnter a valid number\nTry Again\n-------")

def mark_as_done(list1, list2):
    i = 1
    for x in list2:
        print(f"{i}) {x}")
        i += 1
    stop1 = False
    while stop1 == False:
        print("\nEnter task number to be marked as done\n")
        inp = input("-> ")
        if inp:
            if inp.isdigit():
                inp = int(inp)
                if inp <= len(list2):
                    list1.append(list2[inp-1])
                    list2.pop(inp-1)
                    print(f"\n---Task {inp} is Marked as done---")
                    stop = False
                    while stop == False:
                        ask = input("\nWant to mark another task?\n[y / n] : ")
                        if ask:
                            if ask == "y":
                                mark_as_done(list1, list2)
                                stop = True
                            elif ask == "n":
                                stop = True
                                stop1 = True
                            else:
                                print("\nEnter either y or n")
                        else:
                            print("\nSeems you didn't enter anything\nTry again")
                else:
                    print("Enter a valid number\nTry Again")
            else:
                print("\nPlease enter a digit")
        else:
            print("Seems you didn't enter anything\nTry Again")

def delete_task(list1, list2):
    print("\nPending Tasks\n")
    i = 1
    for pending_task in list2:
        print(f"Task {i} - {pending_task}")
        i += 1
    print("\n--------\nDone Tasks\n")
    j = 1
    for done_task in list1:
        print(f"Task {j} - {done_task}")
        j += 1
    stop2 = False
    while stop2 == False:
        inp = input("\nWhich type of task do you want to delete\n1. Pending Task\n2. Done Task\n-> ")
        if inp and inp.isdigit():
            inp = int(inp)
            if inp == 1:
                if len(list2) != 0:
                    s = 1
                    for pending_task in list2:
                        print(f"Task {s} - {pending_task}")
                        s += 1
                    stop = False
                    while stop == False:
                        remove_inp = input("\nWhich task you want to remove\n-> ")
                        if remove_inp and remove_inp.isdigit():
                            remove_inp = int(remove_inp)
                            if remove_inp <= len(list2):
                                list2.pop(remove_inp-1)
                                print("\n---Task Removed Successfully---")
                                stop1 = False
                                while stop1 == False:
                                    ask = input("\nWant to remove more tasks ?\n[y/n] : ")
                                    if ask:
                                        if ask == "y":
                                            delete_task(list1, list2)
                                            stop1 = True
                                        elif ask == "n":
                                            stop1 = True
                                            stop = True
                                            stop2 = True
                                        else:
                                            print("\nEnter either y / n")
                                    else:
                                        print("\nSeems you didn't enter anything\nTry Again")
                            else:
                                print("\nInvalid input\nTry Again")
                        else:
                            print("\nInvalid Input\nTry Again")
                else:
                    print("\nNo Tasks Available To delete\nList is empty")
            elif inp == 2:
                if len(list1) != 0:
                    s = 1
                    for done_task in list1:
                        print(f"Task {s} - {done_task}")
                        s += 1
                    stop = False
                    while stop == False:
                        remove_inp = input("\nWhich task you want to remove\n-> ")
                        if remove_inp and remove_inp.isdigit():
                            remove_inp = int(remove_inp)
                            if remove_inp <= len(list1):
                                list1.pop(remove_inp-1)
                                print("\n---Task Removed Successfully---")
                                stop1 = False
                                while stop1 == False:
                                    ask = input("\nWant to remove more tasks ?\n[y/n] : ")
                                    if ask:
                                        if ask == "y":
                                            delete_task(list1, list2)
                                            stop1 = True
                                        elif ask == "n":
                                            stop1 = True
                                            stop = True
                                            stop2 = True
                                        else:
                                            print("\nEnter either y / n")
                                    else:
                                        print("\nSeems you didn't enter anything\nTry Again")
                            else:
                                print("\nIncalid Input\nTry again")
                        else:
                            print("\nSeems you didn't enter anything\nTry Again")
                else:
                    print("\nNo task is available to delete\nList is empty")
            else:
                print("\nEnter [1 or 2]\n------------")
        else:
            print("\nSeems you didn't enter anything\nTry Again")

def view_all_list(list1, list2):
    stop = False
    while stop == False:
        ask_type = input("\nWhich Task list you want to see\na. Pending Tasks\nb. Done Tasks\nc. Both\n-> ")
        if ask_type:
            if ask_type == "a":
                if len(list2) != 0:
                    print("\nPending Tasks\n")
                    i = 1
                    for task in list2:
                        print(f"{i}) {task}")
                    stop2 = False
                    while stop2 == False:
                        ask = input("\nWant to see another list ?\n-> ")
                        if ask:
                            if ask == "y":
                                view_all_list(list1, list2)
                            elif ask == "n":
                                print("\nHave a nice day\n----------")
                                stop2 = True
                                stop = True
                            else:
                                print("\nEnter either y / n")
                        else:
                            print("\nSeems you didn't enter anything\nTry Again")
                else:
                    print("\n- No pending tasks\nWell Done !!")
                    stop = True
            elif ask_type == "b":
                if len(list1) != 0:
                    print("\nDone Tasks\n")
                    i = 1
                    for task in list1:
                        print(f"{i}) {task}")
                    stop2 = False
                    while stop2 == False:
                        ask = input("\nWant to see another list ?\n-> ")
                        if ask:
                            if ask == "y":
                                view_all_list()
                            elif ask == "n":
                                print("\nHave a nice day\n----------")
                                stop2 = True
                                stop = True
                            else:
                                print("\nEnter either y / n")
                        else:
                            print("\nSeems you didn't enter anything\nTry Again")
                else:
                    print("\n- No tasks Available")
            elif ask_type == "c":
                print("\n--------\nPending Tasks\n")
                if len(list2) != 0:
                    i = 1
                    for task in list2:
                        print(f"{i}) {task}")
                        i += 1
                else:
                    print("No Pending Tasks")
                print("\n--------\nDone Tasks\n")
                if len(list1) != 0:
                    i = 1
                    for task in list1:
                        print(f"{i}) {task}")
                        i += 1
                    stop = True
                else:
                    print("No Tasks Available")
                    stop = True
            else:
                print("\nEnter either [a or b]")
        else:
            print("Enter Valid Input\nTry Again")

def to_do_list():

    pending = []
    done = []

    home_page()
    stop = False
    while stop == False:
        print("\n0. To exit the Program\n1. Add new Tasks\n2. Mark tasks as done\n3. Delete Tasks\n4. View all tasks\n  a. Pending\n  b. Done\n  c. Both")
        inp = input("\nEnter your response here -> ")
        if inp:
            if inp.isdigit():
                inp = int(inp)
                if inp == 1:
                    add_new_task(done, pending)
                elif inp == 2:
                    if len(pending) != 0:
                        mark_as_done(done, pending)
                        continue
                    elif len(pending) == 1:
                        done.append(pending[inp-1])
                        pending.pop(inp-1)
                        print(f"\n---Task is Marked as done---")
                    else:
                        print("\nList is Empty")
                elif inp == 4:
                    view_all_list(done, pending)
                elif inp == 3:
                    delete_task(done, pending)
                elif inp == 0:
                    print("\nHave a nice day")
                    stop = True
                else:
                    print("\nEnter the valid digit")
            else:
                print("\nEnter a Digit")
        else:
            print("\nSeems you didn't enter anything\nTry Again\n-------")

to_do_list()
