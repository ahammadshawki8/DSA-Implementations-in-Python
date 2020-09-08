filepath = input("Enter the file path\n")
freq = {}
for piece in open(filepath).read().lower().split(): # we have to define the path of the file
    # only consider alphabeticcal character within this piece
    word = "".join(c for c in piece if c.isalpha())
    if word:    #require alleast one alphabetical character
        freq[word] = 1 + freq.get(word, 0)


max_word = ""
max_count = 0
for (w,c) in freq.items():      # (key,value) tuples represents (words,counts)
    if c > max_count:
        max_word = w
        max_count = c

print("The most frequent word is", max_word)
print("Its number of occurences is", max_count)
