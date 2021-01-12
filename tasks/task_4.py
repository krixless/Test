def func(string):
 numbers = []
 for i in string:
     if i.isdigit():
         numbers.append(i)
 return print(numbers)

func('123asd1212ad222')