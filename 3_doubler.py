name = input('Enter a frase: ')
b = ' '
for i in range(len(name)):
    b = (b + name[i] * 2)
    if name[i] == ' ':
        continue
print(b)
