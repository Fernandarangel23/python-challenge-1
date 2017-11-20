import os
import csv

# declare lists
words, sentences, letters = ([] for i in range(3))

txt_path = os.path.join('raw_data', 'paragraph_2.txt')


with open(txt_path, mode='r', newline='') as paragraph:
    word_reader = csv.reader(paragraph, delimiter=' ')

    for word in word_reader:
        words = word


with open(txt_path, mode='r', newline='') as paragraph:
    sentence_reader = csv.reader(paragraph, delimiter='.')

    for sentence in sentence_reader:
        sentences = sentence


with open(txt_path, mode='r', newline='') as paragraph:

    reader = paragraph.read().replace(' ', '').replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('-', '').replace('>', '').replace('<', '').replace('=', '')

    letters = reader


# *-----------------*
# |  Summary Table  |
# *-----------------*

print("\nParagraph Analysis")
print("-" * 40)
print("Approximate Word Count:", len(words))
print("Approximate Sentence Count:", len(sentences) - 1)
print("Average Letter Count:", round(len(letters) / len(words), 4), "per word")
print("Average Sentence Length:", round(len(words) / len(sentences), 4), "words")
print("\n\n")

print(words)
print(sentences)
