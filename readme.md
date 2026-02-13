# Stream Cipher – Parte 1.1  
## Generación del Keystream

### Descripción

En esta sección se implementa una función para generar un **keystream pseudoaleatorio determinístico** utilizando un generador de números pseudoaleatorios (PRNG) básico.

El keystream se utilizará posteriormente en un esquema de cifrado tipo stream cipher mediante la operación XOR.

La función cumple con los siguientes requisitos:

- Utiliza un PRNG básico (`random.Random`)
- Acepta una clave (`seed`) como parámetro
- Genera un keystream de longitud igual o mayor al mensaje
- Es determinística (misma clave ⇒ mismo keystream)