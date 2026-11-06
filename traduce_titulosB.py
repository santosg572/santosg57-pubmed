file = 'titulos.txt'

from deep_translator import GoogleTranslator

traductor = GoogleTranslator(source="en", target="es")

fil = open(file, 'r')

datos = fil.readlines()

traducidas = traductor.translate_batch(datos)

k = 1
for ss in traducidas:
  ss = ss.replace('\n','')
  print(ss)


