# Funktion, die die Zeilen einer Datei liest und sie entsprechend formatiert
def format_lines(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_filename, 'w', encoding='utf-8') as file:
        for line in lines:
            # Entferne den Zeilenumbruch am Ende, füge Anführungszeichen hinzu und schreibe in die neue Datei
            formatted_line = f'"{line.strip()}",\n'
            file.write(formatted_line)


# Hier setzt du die Namen der Eingabe- und Ausgabedateien
input_filename = 'input.txt'
output_filename = 'output.txt'

# Rufe die Funktion mit den Dateinamen auf
format_lines(input_filename, output_filename)