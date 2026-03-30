def find_keyword_lines(filename, keyword):
    line_numbers = []
    with open(filename, 'r', encoding='utf-8') as f:
        for index, line in enumerate(f, start=1):
            if keyword in line:
                line_numbers.append(index)
    return line_numbers