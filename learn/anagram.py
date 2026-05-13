# Anagram Check
# This program takes any two words from the user and checks if they are anagrams.

# Taking the input:
word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()

if sorted(word1) == sorted(word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print("Not anagrams.")