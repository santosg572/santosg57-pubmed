from Bio import Entrez


def buscar_y_descargar_pubmed(termino_busqueda, max_resultados=1000):
    # Siempre debes proporcionar tu correo electrónico al usar la API de NCBI
    Entrez.email = "santosg@gmail.com"

    print(f"Buscando '{termino_busqueda}' en PubMed...")

    # 1. Buscar en PubMed para obtener los IDs de los artículos
    handle_busqueda = Entrez.esearch(
        db="pubmed", term=termino_busqueda, retmax=max_resultados
    )
    resultados_busqueda = Entrez.read(handle_busqueda)
    handle_busqueda.close()

    id_list = resultados_busqueda["IdList"]

    if not id_list:
        print("No se encontraron artículos.")
        return

    print(f"Se encontraron {len(id_list)} artículos. Descargando detalles...")

    # 2. Usar los IDs para descargar la información completa
    ids_comas = ",".join(id_list)
    handle_detalles = Entrez.efetch(
        db="pubmed", id=ids_comas, retmode="xml", rettype="abstract"
    )
    articulos = Entrez.read(handle_detalles)
    handle_detalles.close()

    # 3. Procesar y mostrar los resultados
    for i, articulo in enumerate(articulos["PubmedArticle"]):
        medline_citation = articulo["MedlineCitation"]
        article_data = medline_citation["Article"]

        titulo = article_data["ArticleTitle"]

        # El resumen (abstract) a veces puede no estar disponible
        abstract_chunks = article_data.get("Abstract", {}).get(
            "AbstractText", []
        )
        abstract = (
            " ".join(abstract_chunks)
            if abstract_chunks
            else "Resumen no disponible."
        )

        print(f"\n--- ARTÍCULO {i+1} ---")
        print(f"ID (PMID): {medline_citation['PMID']}")
        print(f"Título: {titulo}")
        print(f"Resumen: {abstract}\n")


# Ejemplo de uso
if __name__ == "__main__":
    # Cambia el término por el que tú quieras buscar
    buscar_y_descargar_pubmed("machine learning", max_resultados=100000)


