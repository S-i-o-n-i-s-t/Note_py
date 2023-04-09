import Add_csv_text as add_t
import datetime

def create_new_note():
    title = input('__Заголовок заметки - ')
    text = input('__Текст заметки - ')
    time = datetime.datetime.now() 
    add_t.add_text(title)
    add_t.add_text(text)
    add_t.add_text(time)

def add_red_text(text):
    add_t.clear_fail()
    for item in text:
        add_t.add_text(item)
    add_t.file_correction()
        
    