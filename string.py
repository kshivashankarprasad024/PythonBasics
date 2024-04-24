word = input()
    n = len(word)
    # n = 8
    # 0 1 2 3 4 5 
for index in range(0, n, 2):
    print(word[index], end = " ")
 
 
 
 
word = input()
vowels = "aeiou"
 
for ch in word:
    if ch not in vowels:
        print(ch)




word = input()
reverseWord = word[::-1]
if word == reverseWord:
    print("Palindrome")
else:
    print("Not a palindrome")
 
 
 
 
 
 
 
 
word = input()
result = 0 
n = len(word)
# n = 8
 
for index in range(n - 1):
    if word[index] == 'a' and word[index + 1] == 'b':
        result += 1 
 
print(result)
 
 
 
 
 
 
 
 
 
 


