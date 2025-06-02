from collections import defaultdict
import re
word_count = defaultdict(int)
with open('song.txt', 'r', encoding='utf-8') as file:
    for line in file:
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            word_count[word] += 1
words_once = [word for word, count in word_count.items() if count == 1]
print(f"Broj riječi koje se pojavljuju samo jednom: {len(words_once)}")
print("Te riječi su:")
print(', '.join(words_once))
