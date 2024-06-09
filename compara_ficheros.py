import difflib

def comparar_ficheros(file1,file2):
    with open(file1, 'r') as file1:
        with open(file2, 'r') as file2:
            with open ("./info/output.txt", "w") as out_file:
                f2_lines = set(file2)
                for line in file1:
                    if line not in f2_lines:
                        out_file.write(line)
                        f2_lines.add(line)