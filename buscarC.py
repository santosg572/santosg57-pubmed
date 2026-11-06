from Bio import Entrez
import json

# REQUISITO OBLIGATORIO DE NCBI: Configura tu correo electrónico
# Esto permite que el NCBI te contacte si hay algún problema con tus solicitudes
Entrez.email = "tu_correo@ejemplo.com"

def buscar_y_descargar_pubmed(autor, fecha_inicio, fecha_fin, max_resultados=10):
    """
    Busca artículos en PubMed por autor y rango de fechas, y extrae su información.
    Formatos de fecha: YYYY/MM/DD o simplemente YYYY
    """
    # 1. Construir la consulta estructurada usando etiquetas de PubMed (tags)
    # [AU] especifica Autor, [DP] especifica Fecha de Publicación (Date of Publication)
    termino_busqueda = f'"{autor}"[AU] AND ("{fecha_inicio}"[DP] : "{fecha_fin}"[DP])'
    
    print(f"Buscando en PubMed: {termino_busqueda}")
    
    # 2. Realizar la búsqueda para obtener los IDs (PMIDs)
    with Entrez.esearch(db="pubmed", term=termino_busqueda, retmax=max_resultados) as handle:
        resultado_busqueda = Entrez.read(handle)
        
    id_list = resultado_busqueda["IdList"]
    print(f"Se encontraron {len(id_list)} artículos.")
    
    if not id_list:
        return []

    # 3. Descargar los detalles completos de los IDs encontrados
    ids_comificados = ",".join(id_list)
    with Entrez.efetch(db="pubmed", id=ids_comificados, retmode="xml") as handle:
        detalles_articulos = Entrez.read(handle)
        
    articulos_procesados = []
    
    # 4. Parsear la estructura XML devuelta por la API
    for articulo in detalles_articulos['PubmedArticle']:
        medline_citation = articulo['MedlineCitation']
        article_info = medline_citation['Article']
        
        # Extraer campos principales de forma segura
        pmid = str(medline_citation['PMID'])
        titulo = article_info.get('ArticleTitle', 'Sin título')
        
        # Obtener el resumen (abstract) si está disponible
        abstract_text = ""
        if 'Abstract' in article_info and 'AbstractText' in article_info['Abstract']:
            abstract_text = " ".join(article_info['Abstract']['AbstractText'])
        
        # Obtener la fecha de publicación estructurada
        fecha_pub = article_info['Journal']['JournalIssue']['PubDate']
        año = fecha_pub.get('Year', 'N/A')
        mes = fecha_pub.get('Month', 'N/A')
        dia = fecha_pub.get('Day', 'N/A')
        fecha_completa = f"{año}-{mes}-{dia}"
        
        articulos_procesados.append({
            "pmid": pmid,
            "titulo": titulo,
            "fecha_publicacion": fecha_completa,
            "resumen": abstract_text
        })
        
    return articulos_procesados

# --- EJEMPLO DE USO ---
if __name__ == "__main__":
    # Parámetros de búsqueda
    autor_buscar = "Barrios FA"          # Formato usual: Apellido Iniciales
    desde_fecha = "2025/01/01"         # Formato: AAAA/MM/DD
    hasta_fecha = "2026/12/31"
    
    resultados = buscar_y_descargar_pubmed(autor_buscar, desde_fecha, hasta_fecha, max_resultados=100)
    
    # Mostrar resultados en formato limpio
    print(json.dumps(resultados, indent=4, ensure_ascii=False))

