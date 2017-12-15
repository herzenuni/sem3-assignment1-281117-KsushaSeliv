#Задача 1 

def function():
  chislo=input('Введите число:')
  return chislo
def sum(chislo):
  spisok=list(chislo) #преобразуем число в список, чтобы потом пробежаться по нему и сосчитать 
  summa=0
  #цикл "пробежки"
  for i in spisok:
    summa += int(i)
  return summa
def prints(ks):
  print('Сумма чисел: {}'.format(ks))
prints(sum(function()))
