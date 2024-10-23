#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan
#nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin
#on muutettava auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta
#suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan
#ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee
#sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua
#matkaa ei tarvitse vielä päivittää.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, t_nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = t_nopeus
        self.kuljettu_matka = matka

    # Kiihdyttää tai vähentää nopeutta annetulla muutoksella kunnes kohdataan min(0) tai max(huippunopeus) nopeus:
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


auto1 = Auto("ABC-123", 142)
print(f"Uuden auton ominaisuudet:\n"
      f"Rekisteritunnus: {auto1.rekisteritunnus}\n"
      f"Huippunopeus: {auto1.huippunopeus} km/h\n"
      f"Tämänhetkinen nopeus: {auto1.tamanhetkinen_nopeus} km/h\n"
      f"Kuljettu matka: {auto1.kuljettu_matka} km")

print()
print("Kiihdytys +30 km/h!")
n_muutos = 30
auto1.kiihdytä(n_muutos)
#print(auto1.tamanhetkinen_nopeus) #Tarkistaa nopeuden muutoksen
print("Kiihdytys +70 km/h!")
n_muutos = 70
auto1.kiihdytä(n_muutos)
#print(auto1.tamanhetkinen_nopeus) #Tarkistaa nopeuden muutoksen
print("Kiihdytys +50 km/h!")
n_muutos = 50
auto1.kiihdytä(n_muutos)
print(f"Nopeus: {auto1.tamanhetkinen_nopeus} km/h")
print()
print("Äkkijarrustus -200 km/h!")
n_muutos = -200
auto1.kiihdytä(n_muutos)
print(f"Nopeus: {auto1.tamanhetkinen_nopeus} km/h")