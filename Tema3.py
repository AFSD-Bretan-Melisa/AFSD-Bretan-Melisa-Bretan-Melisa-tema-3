meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
cantitati = {"papanasi": 10, "ceafa": 3, "guias": 6}  # inventar

for student in studenti:
    if comenzi and tavi:  # Verificăm dacă avem comenzi și tăvi disponibile
        comanda = comenzi.pop(0)  # preluăm comanda din coadă
        tava = tavi.pop()  # luăm o tava din stivă
        print(f"{student} a comandat {comanda}.")
        istoric_comenzi.append(comanda)  # actualizăm istoricul
        cantitati[comanda] -= 1  # scădem din inventar

from collections import Counter

comenzi_count = Counter(istoric_comenzi)
print("S-au comandat:", end=" ")
for produs, cantitate in comenzi_count.items():
    print(f"{cantitate} {produs}", end=", ")
print("\n")

print(f"Mai sunt {len(tavi)} tavi.")

for produs in ['ceafa', 'papanasi', 'guias']:
    print(f"Mai este {produs}: {cantitati[produs] > 0}.")

total = 0
for comanda in istoric_comenzi:
    for produs in preturi:
        if produs[0] == comanda:
            total += produs[1]

print(f"Cantina a încasat: {total} lei.")

produse_sub_7 = [produs for produs in preturi if produs[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_sub_7}.")
