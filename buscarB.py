from Bio import Entrez

# 1. Configura tu correo electrónico (obligatorio por normas del NCBI)
Entrez.email = "santosg572@gmail.com"

# (Opcional) Si tienes una API Key gratuita de tu cuenta de NCBI, ponla aquí para hacer más consultas por segundo
# Entrez.apikey = "tu_api_key_de_ncbi"

# 2. Realiza la búsqueda (esearch) para obtener los IDs de PubMed
termino_busqueda = "machine learning in medicine AND 2025[pdat]"
handle = Entrez.esearch(db="pubmed", term=termino_busqueda, retmax=5)
registro = Entrez.read(handle)
handle.close()

id_list = registro["IdList"]
print(f"IDs encontrados: {id_list}")

# 3. Descarga los detalles de los artículos (efetch)
if id_list:
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="text")
    datos_medline = handle.read()
    handle.close()
    
    # Muestra una vista previa de los datos descargados
    print(datos_medline[:1500])
    
    # Opcional: Guardar los resultados en un archivo de texto plano
    with open("referencias_pubmed.txt", "w", encoding="utf-8") as f:
        f.write(datos_medline)
    print("\n¡Referencias guardadas exitosamente en 'referencias_pubmed.txt'!")

