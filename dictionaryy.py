word = input()
print(word)
store = dict()
for ch in word:
    if ch in store:
        store[ch] = store[ch] + 1
    else:
        store[ch] = 1
print(store)

resultChar = '#'
resultFrequency = 0
allKeys = store.keys()
for ele in allKeys:
    if store[ele] > resultFrequency:
        resultFrequency = store[ele]
        resultChar = ele

print(resultChar, resultFrequency)
