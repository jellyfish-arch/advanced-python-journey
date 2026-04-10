text = input("Enter a sentence: ")
words = text.split()

print("Word count:", len(words))
print("Characters:", len(text))
print("Unique words:", len(set(words)))
