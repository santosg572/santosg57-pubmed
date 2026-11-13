from Bio import Entrez, Medline

# 1. Configura tu correo (obligatorio por la política de NCBI)
Entrez.email = 'tu_correo@ejemplo.com'

# Opcional: si tienes una API key de NCBI, agrégala aquí para mayor velocidad
# Entrez.api_key = 'TU_API_KEY_DE_NCBI'

termino_busqueda = 'fmri'
max_resultados = 10000

# 2. Buscar artículos en PubMed (esearch)
handle_busqueda = Entrez.esearch(
    db='pubmed',
    term=termino_busqueda,
    retmax=max_resultados
)
resultado_busqueda = Entrez.read(handle_busqueda)
handle_busqueda.close()

lista_pmids = resultado_busqueda['IdList']
print(f"Total de registros encontrados: {resultado_busqueda['Count']}")
print(f"PMIDs obtenidos: {lista_pmids}\n")

# 3. Descargar los detalles de los artículos (efetch)
if lista_pmids:
  handle_lectura = Entrez.efetch(
      db='pubmed', id=lista_pmids, rettype='medline', retmode='text'
  )
  registros = Medline.parse(handle_lectura)

  for record in registros:
    print(f"Título: {record.get('TI', '?')}")
    print(f"Autores: {', '.join(record.get('AU', []))}")
    print(f"Revista: {record.get('JT', '?')}")
    print(f"Año: {record.get('DP', '?')}")
    print('-' * 40)
  handle_lectura.close()


