import random
import hashlib

def generar_keystream(seed: str, longitud: int) -> bytes:
   
    if longitud < 0:
        raise ValueError("La longitud debe ser >= 0")

    seed_bytes = seed.encode("utf-8")
    seed_int = int.from_bytes(hashlib.sha256(seed_bytes).digest(), byteorder="big")

    rng = random.Random(seed_int)
    return bytes(rng.randrange(0, 256) for _ in range(longitud))


if __name__ == "__main__":
    ks1 = generar_keystream("mi-clave", 16)
    ks2 = generar_keystream("mi-clave", 16)
    ks3 = generar_keystream("otra-clave", 16)

    print(ks1)           
    print(ks1.hex())       
    print(ks1 == ks2)      # True (mismo seed => mismo keystream)
    print(ks1 == ks3)      # False
