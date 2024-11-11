text = input("Enter a sentence: ")
text = text.split()
max = text[0]
for i in text:
    if i > max:
        max = i
        
print("Longest word is :", max)