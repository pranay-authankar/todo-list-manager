def input_all(message):
    while True:
        print(f"\n{message}", end=" ")
        inp = input("-> ")
        if inp:
            return inp
        else:
            print("\nError : You didn't enter anything\nTry again with some input\n")

def input_alpha(message):
    while True:
        inp = input_all(message)
        if inp.isalpha():
            return inp
        else:
            print("\nError : Enter only alphabetical value\n")

def input_int(message):
    while True:
        inp = input_all(message)
        if inp.isdigit():
            return int(inp)
        else:
            print("\nError : Enter only numeric value\n")

def input_specific_int(message, start, stop):
    while True:
        inp = input_int(message)
        if start <= inp <= stop:
            return int(inp)
        else:
            print(f"\nError : Enter numeric value between [{start} - {stop}]\n")

def input_alnum(message):
    while True:
        inp = input_all(message)

        if inp.isdigit():
            return int(inp)
        elif inp.isalnum():
            return inp
        else:
            print("\nError : Enter only alphanumeric value\n")

def yes_no(message):
    while True:
        inp = input_alpha(message).lower()

        if inp in "yn":
            match inp:
                case "y":
                    return True
                case "n":
                    return False
        else:
            print("\nEnter only [y / n]\n")

def center(message, size, fill, ends):
    print(f"{f"{message}".center(size, fill)}", end = ends)

def table_data(column_header, column_data):

    row_data = dict.fromkeys(column_header)

    i = 0

    for outer in column_data:
        row_data[column_header[i]] = outer
        i += 1
    
    return row_data

def table_formatting(column, cell, heading, row_data):

    cell_length = cell

    shift = column - 1

    table_size = column * cell_length + shift

    if table_size > 160:
        print(f"\nInfo: Currenet Table Size = {table_size} | Limit = 160\nTry Again within the limit\n")
        return

        
    center("=", (column * cell_length) + shift, "=", "|\n")
    center(f"{heading}", (column * cell_length) + shift, " ", "|\n")
    center("=", (column * cell_length) + shift,  "=", "|\n")

    for head in row_data:
        center(head, cell_length, " ", "|")
    print("")

    for i in range(column):
        center("=", cell_length, "=", "|")
    print("")


    i = 0
    j = 0

    key = list(row_data.keys())[i]

    while j < len(row_data[key]):
        i = 0
        while i < len(row_data):
            key = list(row_data.keys())[i]
            center(row_data[key][j], cell_length, " ", "|")
            i += 1
        j += 1
        print("")
    


    center("=", (column * cell_length) + shift, "=", "|\n")


