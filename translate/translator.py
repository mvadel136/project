import sys

def translate_line(line):
    translations = {
        "ف'الجولة {الجولة_الحالية}:'" : "f'Round {round}:'",
        'شبكة': 'grid',
        'جولات': 'rounds',
        'الجولة_الحالية': 'current_round',
        'بينما': 'while',
        'في': 'in',
        'نطاق': 'range',
        'لكل': 'for',
        'شبكة_جديدة': 'new_grid',
        'الجيران_الأحياء': 'living_neighbors',
        'دس': 'dx',
        'دص': 'dy',
        'نس': 'nx',
        'نص': 'ny',
        'استمر': 'continue',
        'إلا إذا': 'elif',
        'إذا': 'if',
        'إلا': 'else',
        'صحيح': 'True',
        'خطأ': 'False',
        'أو': 'or',
        'و': 'and',
        'طباعة': 'print',
        'نهاية': 'end',
        'آخر': 'else',
        'لجيران_الأحيا': 'living_neighbors',
    }

    for arabic, english in translations.items():
        line = line.replace(arabic, english)

    line = line.replace("[[0 لكل _ في نطاق(8)] لكل _ في نطاق(8)]", "[[0 for _ in range(8)] for _ in range(8)]")

    return line

def translate_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        translated_lines = [translate_line(line) for line in lines]
        translated_code = ''.join(translated_lines)

        exec(translated_code)  
    except FileNotFoundError:
        print(f"File {file_path} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python translator.py <file_name>")
        sys.exit(1)

    file_path = sys.argv[1]
    translate_file(file_path)