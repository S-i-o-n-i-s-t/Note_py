import Sorting_note as s_n
import Main_menu as m_m

def print_notes_text():
    s_n.print_notes()
    m_m.start_menu()

def print_not(x):
    y = 0
    path = 'output.csv'
    with open(path, 'r') as main_file:  
        for item in main_file:
            if y == (x*3):    
                print(item)
            elif y == x*3 + 1:  
                print(item)
            elif y == x*3 + 2:  
                print(item)                 
            y += 1
    m_m.start_menu() 