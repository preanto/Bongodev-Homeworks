a = input("Enter a word: ")
v="aeiouAEIOU"
c="qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
vowel=0
consonent=0
for i in a:
    if i in v:
        vowel = vowel + 1
    elif i in c:
        consonent = consonent + 1
print("Total Vowels: ", vowel)
print("Total Consonents: ", consonent)