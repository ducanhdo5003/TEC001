def analyze_text(text):
    words = text.lower().split()
    total_count = len(words)

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    sorted_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    top_five = dict(sorted_words[:5])

    top_five_sum = sum(top_five.values())
    proportion = (top_five_sum / total_count) * 100 if total_count > 0 else 0

    print(f"Top 5: {top_five}")
    print(f"Total number of words: {total_count}")
    print(f"Proportion of 5 most common words: {top_five_sum} / {total_count} = {proportion:.2f}%")


sample_text = "the world is mine and the world is great because the world is the world"
analyze_text(sample_text)