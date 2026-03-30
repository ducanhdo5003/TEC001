def count_non_blank_lines(filename):
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                count += 1
    return count