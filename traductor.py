import time
from deep_translator import GoogleTranslator
from tqdm import tqdm

translator = GoogleTranslator(source='en', target='es')

archivo_entrada = 'frases_en.txt'
archivo_salida = 'frases_es.txt'

with open(archivo_entrada, 'r', encoding='utf-8') as f:
    frases = [linea.strip() for linea in f if linea.strip()]

with open(archivo_salida, 'a', encoding='utf-8') as f_out:
    for frase in tqdm(frases, desc="Traduciendo"):
        try:
            traduccion = translator.translate(frase)
            f_out.write(traduccion + '\n')
            f_out.flush()
            # Pausa breve para evitar bloqueos por límite de peticiones (rate limit)
            time.sleep(0.3) 
        except Exception as e:
            f_out.write(f"[ERROR: {frase}]\n")
            time.sleep(2)


