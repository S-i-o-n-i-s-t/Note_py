def add_text(text):
    with open('text.csv', 'a') as main_file:
        main_file.write(f'\n{text}')

def clear_fail(text = ''):
    with open('text.csv', 'w') as main_file:
        main_file.write(text)

def file_correction():
    with open("text.csv", 'r') as r, open('output.csv', 'w') as o:
        for line in r:
            if line.strip():
                o.write(line)

def file_revers_correction():
    with open("output.csv", 'r') as r, open('text.csv', 'w') as o:
        for line in r:
            if line.strip():
                o.write(line)
