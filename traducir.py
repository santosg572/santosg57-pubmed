from translate import Translator

# Configura el idioma de origen (inglés: 'en') y destino (español: 'es')
translator = Translator(from_lang="en", to_lang="es")

texto_ingles = "Hello, how are you?"
traduccion = translator.translate(texto_ingles)

print(f"Original: {texto_ingles}")
print(f"Traducido: {traduccion}")


