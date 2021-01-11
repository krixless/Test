word = input('Введите своё слово: ')
word = word.replace(' ','').replace('.','').replace(',','').lower()
if word == word [::-1]:
    print('Palindrome')
else:
    print('Oh no!')s