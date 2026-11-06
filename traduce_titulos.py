file = 'titulos.txt'
from translate import Translator

translator = Translator(from_lang="en", to_lang="es")

fil = open(file, 'r')

datos = fil.readlines()

k = 1
for ss in datos:
  ss = ss.replace('\n','')
  print(ss)
  traduccion = translator.translate(ss)
  print(traduccion)


