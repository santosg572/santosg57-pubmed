from pymed import PubMed

pubmed = PubMed(tool='MyPythonTool', email='lgs@gunam.mx')

# Realiza la consulta
results = pubmed.query('machine learning in medicine', max_results=5)

print(help(results.from_iterable))

for article in results:
  print(f"Título: {article.title}")
  print(f"Autores: {article.authors}")
  print(f"Resumen: {article.abstract}\n{'-'*40}")


