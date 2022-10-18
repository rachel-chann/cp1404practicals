"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 30 minutes
Actual:   32 minutes
"""

text = input('Text: ')
words = text.split(' ')
word_to_count = {}
for word in words:
    occurrence = word_to_count.get(word, 0)
    word_to_count[word] = occurrence + 1
max_length = max((len(word) for word in words))
for word, count in sorted(word_to_count.items()):
    print(f'{word:{max_length}} : {count}')
