def calculate_average_score(filename):
    total_score = 0
    student_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                name, score = line.strip().split(',')
                total_score += float(score)
                student_count += 1

    if student_count == 0:
        return 0
    return total_score / student_count