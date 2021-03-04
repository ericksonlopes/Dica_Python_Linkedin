import winsound

lista = []

with open('music.txt', 'r') as arquivo:
    lines = arquivo.readlines()

    for index, _ in enumerate(lines):
        if index % 2 == 0:
            winsound.Beep(int(lines[index].replace('\n', '')), int(lines[index + 1].replace('\n', '')))
