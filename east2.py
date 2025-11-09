text = input()
t = list(text)
sum = 0
i = 0

while i < len(t) :
    if t[i] == "a" or t[i] == "A" or t[i] == "e" or t[i] == "E" or t[i] == "i" or t[i] == "I" or t[i] == "o" or t[i] == "O" or t[i] == "u" or t[i] == "U" :
        sum += 1
    i += 1

print(sum)