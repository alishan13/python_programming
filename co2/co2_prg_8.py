words=["teenager","appoint","obese","cemetery"]
length = 0;
for word in words:
    if len(word) > length:
        length = len(word)
        largest = word
print(largest)
        