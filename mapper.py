#!/usr/bin/env python3
"""Mapper para WordCount con Hadoop Streaming."""
import sys

# Hadoop Streaming envía cada línea del split de entrada por stdin
for line in sys.stdin:
    line = line.strip()

    # Normalizamos a minúsculas para no contar "Casa" y "casa" por separado
    line = line.lower()

    # Separamos por espacios en blanco (tabs, saltos, espacios múltiples, etc.)
    words = line.split()

    for word in words:
        # Quitamos signos de puntuación pegados a la palabra
        word = word.strip('.,;:!?"\'()[]{}')
        if word:
            # Emitimos el par clave-valor separado por TAB (formato esperado por Hadoop)
            print(f"{word}\t1")
