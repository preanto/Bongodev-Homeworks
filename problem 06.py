a = input("Enter a word: ").lower()
a_list = list(a)
a_dup = a_list.copy()
a_new = []
for i in reversed(a_dup):
    a_new.append(i)

if ( a_new == a_dup ):
    print("Palindrome: True")
else:
    print("Palindrome: False")