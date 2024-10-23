#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
# tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, t_nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = t_nopeus
        self.kuljettu_matka = matka

    # Lisää tai vähentää nopeutta annetulla muutoksella kunnes kohdataan min(0) tai max(huippunopeus) nopeus:
    def kiihdytä(self, nopeuden_muutos):
        if nopeuden_muutos < 0:
            toistot = nopeuden_muutos * -1
        else:
            toistot = nopeuden_muutos
        for i in range(toistot):
            if self.tamanhetkinen_nopeus < self.huippunopeus and nopeuden_muutos >= 0:
                self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus + 1
            elif nopeuden_muutos < 0 and self.tamanhetkinen_nopeus > 0:
                self.tamanhetkinen_nopeus = self.tamanhetkinen_nopeus - 1

    def kulje(self, tunnit):
        matkan_kasvu = self.tamanhetkinen_nopeus * tunnit
        self.kuljettu_matka = self.kuljettu_matka + matkan_kasvu


auto1 = Auto("ABC-123", 142)
print(f"Uuden auton ominaisuudet:\n"
      f"Rekisteritunnus: {auto1.rekisteritunnus}\n"
      f"Huippunopeus: {auto1.huippunopeus} km/h\n"
      f"Tämänhetkinen nopeus: {auto1.tamanhetkinen_nopeus} km/h\n"
      f"Kuljettu matka: {auto1.kuljettu_matka} km")
print()
print("Kiihdytys +30 km/h! Kuljetaan tällä nopeudella 2 tuntia.")
n_muutos = 30
auto1.kiihdytä(n_muutos)
#print(auto1.tamanhetkinen_nopeus) #Tarkista nopeuden muutos!
auto1.kulje(2)
#print(auto1.kuljettu_matka) #Tarkista kuljetun matkan muutos!
print("Kiihdytys +70 km/h! Kuljetaan tällä nopeudella 0,5 tuntia.")
n_muutos = 70
auto1.kiihdytä(n_muutos)
#print(auto1.tamanhetkinen_nopeus) #Tarkista nopeuden muutos!
auto1.kulje(0.5)
#print(auto1.kuljettu_matka) #Tarkista kuljetun matkan muutos!
print("Kiihdytys +50 km/h! Kuljetaan tällä nopeudella 1,5 tuntia.")
n_muutos = 50
auto1.kiihdytä(n_muutos)
auto1.kulje(1.5)
print(f"Nopeus: {auto1.tamanhetkinen_nopeus} km/h")
print(f"Kuljettu matka: {auto1.kuljettu_matka} km")
print()
print("Äkkijarrustus -200 km/h!")
n_muutos = -200
auto1.kiihdytä(n_muutos)
print(f"Nopeus: {auto1.tamanhetkinen_nopeus} km/h")