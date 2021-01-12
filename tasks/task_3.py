import os
fname = input('Введите названия для файла: ')
file = open(fname + '.txt', "w")
file1 = file.write(input('Введите свой текст: '))
file.close()
file = open(fname + '.txt')
file.read()
file.close()
os.remove(fname + '.txt')