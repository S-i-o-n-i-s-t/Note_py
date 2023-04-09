import Add_csv_text
import Add_note as a_n
import Read_note as r_n
import Sorting_note as s_n

def start_menu():
    print('__"Режим просмотра заметок": нажмите - 1__ __"Режим редактирования заметок": нажмите - 2__ __Для выхода введите: другое число__')
    while True:
        try:
            menu = int(input())
            if menu == 1:
                menu_print()
            elif menu == 2:
                main_meny()
            else:
                exit()
        except ValueError:
            print("Не верный символ, попробуйте еще раз")


def menu_print():
    print('__Для просмотра списка заметок: введите - -1__ __Для просмотра нужной вам заметки: введите "индекс заметки"__ __Для выхода в основное меню: введите любое "другое" число')
    
    while True:
        try:
            menu = int(input())
            if menu == -1:
                r_n.print_notes_text()
            elif menu >=0 and menu <= len(s_n.list_text()):
                r_n.print_not(menu)
            else:
                start_menu()
        except ValueError:
            print("__Не верный символ, попробуйте еще раз__")

def main_meny():
    print('__Добавить заметку: нажмите - 1__ __Редактировать заметку: нажмите - 2__ __Удалить заметку: нажмите - 3__ __Для выхода в основное меню: другое число__')
    while True:
        try:
            menu = int(input())
            if menu == 1:
                a_n.add_note()
                Add_csv_text.file_revers_correction()
            elif menu == 2:
                a_n.edit_note()
                Add_csv_text.file_revers_correction()
            elif menu == 3:
                a_n.delete_note()
                Add_csv_text.file_revers_correction()
            else:
                Add_csv_text.file_revers_correction()
                start_menu()
        except ValueError:
            print("Не верный символ, попробуйте еще раз")