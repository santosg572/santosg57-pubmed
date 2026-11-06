file = 'dd.txt'

fil = open(file, 'r')

datos = fil.readlines()

k = 1
for ss in datos:
  ss = ss.replace('\n','')
  ss1 = ss[0:6]
  if ss1 == 'Título':
#    print(str(k) + ' - ' +ss)
    print(ss)
    k=k+1
