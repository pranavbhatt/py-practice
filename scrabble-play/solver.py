import scrabble
import string

# print all words containing "uu"
for word in scrabble.word_list:
    if "uu" in word:
        print(word)

# print all letters that never appear doubled
for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.word_list:
        if letter * 2 in word:
            exists = True
            break
    if not exists:
        print("There are no English words with a double {}".format(letter))

# find all words which contain all vowels
VOWELS = "aeiou"


def has_all_vowels(word):
    for vowel in VOWELS:
        if vowel not in word:
            return False
    return True


for word in scrabble.word_list:
    if has_all_vowels(word):
        print("Word with all vowels is : {}".format(word))

# find the longest palindromes
longest_word = ""

for word in scrabble.word_list:
    if word != word[::-1]:
        if len(word) > len(longest_word):
            longest_word = word

print("{} is the longest palindrome".format(longest_word))

