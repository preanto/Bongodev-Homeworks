sentence = input("Enter a url to check file name: ")
sentence = sentence.split("/")
l = len(sentence)
print("The name of the file is: ",sentence[l-1])
