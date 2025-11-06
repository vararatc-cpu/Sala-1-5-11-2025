#Sala 1

integrantes = [
"Victor Samuel Ararat Castro",
"Alex Vinicio Albán Cedeño",
"JEFFERSON JAIME FARIAS HERNANDEZ",
"MEISY LISBETH CHOMPOL HOLGUIN",
"RAUL FERNANDO TRUJILLO VERA",
"LUIS ENRIQUE ALVAREZ MEJIA",
"MIRELLA ANTONIA CRISTOBA MEDINA",
"MARK ANTHONY SANCHEZ GOMEZ",
"OSCAR ADRIAN JIMENEZ COX",
"CARLOS DARIO FUENTES ORTEGA",
"SILVIA PAOLA BARRETO MORA",
""
]

#mostrar la lista ordenada por consola
def mostrar_integrantes(integrantes):
    integrantes_ordenados = sorted(integrantes)
    for nombre in integrantes_ordenados:
        print(nombre)

mostrar_integrantes(integrantes)
