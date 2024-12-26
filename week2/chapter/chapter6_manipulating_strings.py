# English to Pig Latin

print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
pigLatin = []  # A list of the words in Pig Latin.

for word in message.split():
    # Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while len(word) > 0 and not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]

    # Remember if the word was in uppercase or title case:
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    # Make the word lowercase for translation:
    word = word.lower()

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # Restore the word's original case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word:
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))


# table printer

def table_printer(table_data):
    col_width = [0] * len(table_data)  # Initialize colWidths with zeros

    # Find the width of the longest string in each column
    for i in range(len(table_data)):
        for j in range(len(table_data[i])):
            col_width[i] = max(col_width[i], len(table_data[i][j]))

    # Print the table
    for j in range(len(table_data[0])):
        for i in range(len(table_data)):
            print(table_data[i][j].rjust(col_width[i]), end=" ")
            # print(table_data[i][j].ljust(col_width[i]), end=" ")

        print()


# Example usage
table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

table_printer(table_data)

