
def list_text():
    title = []
    text = []
    time = []
    x = 1
    path = 'output.csv'
    with open(path, 'r') as main_file:  
        for item in main_file:
            if x == 1:
                title.append(item)
                x +=1
            elif x==2:
                text.append(item)
                x +=1
            elif x == 3:
                time.append(item)
                x = 1
    zip_text = list(zip(title, text, time))
    return zip_text

def print_notes():
    for i, item in enumerate(list_text()):
        print(f'Индекс - {i}')
        print(item)
