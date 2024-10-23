#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus
# ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua
# parametreina saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti
# nollaksi. Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, t_nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = t_nopeus
        self.kuljettu_matka = matka


auto1 = Auto("ABC-123", 142)
print(f"Uuden auton ominaisuudet:\n"
      f"Rekisteritunnus: {auto1.rekisteritunnus}\n"
      f"Huippunopeus: {auto1.huippunopeus} km/h\n"
      f"Tämänhetkinen nopeus: {auto1.tamanhetkinen_nopeus} km/h\n"
      f"Kuljettu matka: {auto1.kuljettu_matka} km")