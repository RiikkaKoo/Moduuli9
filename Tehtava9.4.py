# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan
# seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein
# seuraavat toimenpiteet:

# > Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
#   Tämä tehdään kutsumalla kiihdytä-metodia.
# > Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin
# auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

class KilpaAuto:

    def __init__(self, rekisteritunnus, huippunopeus, t_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = t_nopeus
        self.kuljettu_matka = kuljettu_matka

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

luotu = 0
numero = 0
kilpa_autot = []
while luotu < 10:
    numero = numero + 1
    auto = KilpaAuto(str(f"ABC-{numero}"), random.randint(100,200))
    kilpa_autot.append(auto)
    luotu = luotu + 1

print("Kilpailu alkaa!")
kilpailu_kaynnissa = True
tunnit = 0
while kilpailu_kaynnissa:
    print()
    for i in kilpa_autot:
        i.kiihdytä(random.randint(-10,15))
        print(f"Kilpa-auton {i.rekisteritunnus} tämänhetkinen nopeus on {i.tamanhetkinen_nopeus} km/h!")

    print()
    tunnit = tunnit + 1
    print(f"Kilpailua on nyt kulunut {tunnit} tuntia!")
    print()

    for i in kilpa_autot:
        i.kulje(1)
        print(f"Kilpa-auto {i.rekisteritunnus} on kulkenut {i.kuljettu_matka} kilometriä!")
        if i.kuljettu_matka >= 10000:
            print()
            print(f"+----------------------------------------------------------------------\n"
                  f"| Kilpa-auto tunnuksella {i.rekisteritunnus} on saavuttanut 10 000 km rajan!\n"
                  f"+----------------------------------------------------------------------")
            print()
            kilpailu_kaynnissa = False

    print("---------------------------------------------------------------------------------------------------")

numero = 0
for i in kilpa_autot:
    print("+---------------------------------------------------------")
    numero += 1
    print(f"| Kilpa-auton numero {numero} ominaisuudet:\n"
          f"|\n"
          f"| Rekisteritunnus: {i.rekisteritunnus}\n"
          f"| Huippunopeus: {i.huippunopeus} km/h\n"
          f"| Viimeisin nopeus: {i.tamanhetkinen_nopeus} km/h\n"
          f"| Kuljettu matka: {i.kuljettu_matka} km")

print("+---------------------------------------------------------")