from collections import Counter
import re


def word_count(file_path):
    # Initialize a Counter to keep track of word counts
    word_counter = Counter()

    # Open the file and process each line
    with open(file_path, 'r') as file:
        for line in file:
            # Convert line to lowercase and split into words
            words = re.findall(r'\b\w+\b', line.lower())
            # Update the word counts
            word_counter.update(words)

    # Print word counts
    for word, count in word_counter.items():
        print(f'{word}: {count}')


# Example usage

    # Provide the path to your text file here
file_path = '/Users/rahul1.patidar/Desktop/files/wordCount.csv'
word_count(file_path)
