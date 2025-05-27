
import random

def pozdrav():
    print("Ahoj, jak se máš?")

def dnesni_den():
    print("Dnes je úterý.")

def vypis_cisla():
    for i in range(1, 6):
        print(i, end=' ')
    print()

def obdelnik():
    for _ in range(3):
        print("*****")

def nalada_dne():
    nalady = ["veselá", "smutná", "unavená", "nadšená", "zamračená"]
    print(f"Dnešní nálada je: {random.choice(nalady)}.")
