#!/usr/bin/env python3
"""Reducer para WordCount con Hadoop Streaming."""
import sys

current_word = None
current_count = 0

# Hadoop Streaming garantiza que las claves llegan ordenadas (shuffle & sort)
# por eso podemos acumular mientras la palabra no cambie.
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        # Ignoramos líneas mal formadas
        continue

    if current_word == word:
        current_count += count
    else:
        # Cambió la clave: volcamos el resultado acumulado de la palabra anterior
        if current_word is not None:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# No olvidar emitir el último grupo acumulado
if current_word is not None:
    print(f"{current_word}\t{current_count}")
