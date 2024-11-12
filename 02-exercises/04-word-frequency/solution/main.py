text = "Hello world hello Guido Coding World HELLO WORLD hElLO gUiDO"
frequency = {}

for word in text.lower().split():
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
