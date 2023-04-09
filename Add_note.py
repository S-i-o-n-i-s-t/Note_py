import Add_csv_text
import Sorting_note as sort_n
import Create_note as cr_n
import Main_menu as m_m

def delete_note():
    Z = selekt_note()
    text = []
    y = 0
    path = 'output.csv'
    with open(path, 'r') as main_file:  
        for item in main_file:
            if y == (Z*3):    
                text.append('')
            elif y == Z*3 + 1:  
                text.append('')
            elif y == Z*3 + 2:  
                text.append('')
            else:
                text.append(item)                  
            y += 1
    cr_n.add_red_text(text)
    m_m.main_meny() 
    
def edit_note():
    Z = selekt_note()
    text = []
    y = 0
    path = 'output.csv'
    with open(path, 'r') as main_file:  
        for item in main_file:
            if y == Z*3 + 1:  
                print('Введите новый текст заметки')  
                text.append(f'{input()}\n')
            else:
                text.append(item)                  
            y += 1     
    cr_n.add_red_text(text)
    m_m.main_meny()

def selekt_note():
    sort_n.print_notes()
    print('__Выберите заметку из списка, и введите ее индекс__')
    x = len(sort_n.list_text())
    while True:
        try:
            num_note = int(input())
            if num_note >= 0 and num_note <= x:
                x = num_note
                return num_note
            else:
                print('__Такого индекса нет__')
                # selekt_note()
                m_m.main_meny()
        except ValueError:
            print("__Не верный символ, попробуйте еще раз__")

def add_note():
    yes = 'n'
    while yes != 'y':
        cr_n.create_new_note()
        print('Если хотите выйти из режима "создаие заметки" введите "y"')
        yes = input()
    Add_csv_text.file_correction()
    m_m.main_meny()

