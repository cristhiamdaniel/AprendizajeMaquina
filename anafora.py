######## Requerimientos #######
'''
spacy==2.1.3
neuralcoref==4.0.0

python3 -m spacy download en_core_web_sm

Cuando trabajamos en problemas de extracción de entidades y relaciones \
de texto, nos enfrentamos con el texto real, y muchas de las entidades \
pueden terminar siendo extraídas como pronombres (el, ella). Para este \
caso se realiza una anáfora, o el proceso de sustitución de los \
pronombres con sus referentes.

'''

# Importamos paquetes
import spacy
import neuralcoref

# Cargamos el motor
nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)

# Definimos el texto
text = "Earlier this year, Nicolas started going to school for\
	the first time. He was very eager to meet new friends.\
	The boy never lost interest in getting to class."

# Procesamos el texto:
doc = nlp(text)
print(doc._.coref_resolved)
