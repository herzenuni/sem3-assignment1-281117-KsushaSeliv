#Задание 2

def function_1(chislo):
  x=str(chislo)
  summa=0
  for i in x:
    summa += int(i)**2
  return summa
  
def function_2():
  for i in range(10, 1000):
    if function_1(i) % 17 == 0:
      print('Числа, сумма цифр которых в квадрате делится на 17: {}' .format(i))

function_2()  
