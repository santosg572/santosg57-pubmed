file = 'abstract-functional-connectivity_ago1726.txt'

fil = open(file, 'r')

datos = fil.readlines()

k = 1
n = 0
while n < 10:
  ss = datos[n]
  ss = ss.replace('\n', '')
  str1 = str(k)+'. '
  if str1 == ss[:3]:
    print('-------------' + ss)
    i = n+1

    ss = datos[i]
    ss = ss.replace('\n', '')
    while len(ss) == 0:
      
  n = n+1

