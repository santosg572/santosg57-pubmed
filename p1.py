file = 'abstract-functional-connectivity_ago1726.txt'

fil = open(file, 'r')

datos = fil.readlines()

ln = len(datos)

k = 1
n = 0

while n < ln:
  ss = datos[n]
  ss = ss.replace('\n', '')
  str1 = str(k)+'. '
  if k < 10:
    if str1 == ss[:3]:
      print('-------------' + ss)
      k = k+1    
  elif k < 100:
    if str1 == ss[:4]: 
      print('-------------' + ss)
      k = k+1
  elif k < 1000:
    if str1 == ss[:5]:
      print('-------------' + ss)
      k = k+1
  else:
    if str1 == ss[:6]:
      print('-------------' + ss)
      k = k+1

  n = n+1

