######################## DISPLAY OPTION FUNCTION:

def display_options():
    options = "(1) View To-Dos (2) Add To-Do (3) Remove To-Do (4) Exit"
    selected_option = int(input(options))
    return selected_option


###################### TO-DO LIST:

to_do_list = ["6:45 AM Swim Practice", "Reply to Mr. Rossum's email", "Walk and Feed Fido"]

#################### FUNCTIONS

def view_to_dos():
    print("_____________________________________")
    print(f"There are {len(to_do_list)} things to do today!😳")
    print(to_do_list)
    print("_____________________________________")

#---------------------------------------------------------------
    
def add_to_do():
    to_do = input("What would you like to add to your to-do list?😊")
    to_do_list.append(to_do)
    print(f"{to_do} has been added to your list!👍")
    
#---------------------------------------------------------------

def remove_to_do():
    view_to_dos()
    index = int(input("Enter the correct index number to remove to do!"))
    remove_to_do = to_do_list.pop(index)
    print(f"{remove_to_do} has been removed!✔️")

    
######################## LOOP:
    
while True:
    selected_option = display_options()
    if selected_option == 1:
        view_to_dos()
    elif selected_option == 2:
        add_to_do()
    elif selected_option == 3:
        remove_to_do()
    elif selected_option == 4:
        print("See ya next time!")
        break

######################## FIN