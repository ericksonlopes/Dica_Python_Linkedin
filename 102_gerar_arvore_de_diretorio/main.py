import os


def generate_directory_tree(root_directory, level=0):
    for name_file in os.listdir(root_directory):
        path = os.path.join(root_directory, name_file)
        if os.path.isfile(path):
            print("|   " * level + "|-- " + name_file)
        elif os.path.isdir(path):
            print("|   " * level + "+-- " + name_file)
            generate_directory_tree(path, level + 1)


generate_directory_tree('C:\\Test')

# [Saída]

# +-- Directory1
# |   +-- File1.txt
# |   +-- File2.txt
# +-- Directory2
# |   +-- Subdirectory1
# |   |   +-- File3.txt
# |   |   +-- File4.txt
# |   +-- Subdirectory2
# |   |   +-- File5.txt
# |   |   +-- File6.txt
# |   +-- File7.txt
# +-- File8.txt
