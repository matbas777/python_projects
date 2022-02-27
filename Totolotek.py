""" Ta aplikacja ma na celu obliczyc Twoje szanse na wygranie glownej nagrody w grze totolotek.
    Wynik jaki otrzymamy to liczba prob osiagniecia danego wyniku. Nagrody z tej gry sa przyznawane za trafienie
    3, 4, 5 i 6 wytypowanych przen nas liczb.
    W zmiennej o nazwie my_numbers znajduje sie 6 Twoich typowanych liczb od 1 do 49.
    Wytypuj swoje liczby i sprawdz za ktorym razem wygrasz glowna nagrode/
     This application aims to calculate your chances of winning the grand prize in the totolotek game."""

import dateparser
from datetime import datetime
import random

print(
    "Ta aplikacja ma na celu obliczyc Twoje szanse na wygranie glownej nagrody w grze totolotek.\n"
    "Wynik jaki otrzymamy to liczba prob osiagniecia danego wyniku.\n"
    " Nagrody z tej gry sa przyznawane za trafienie 3, 4, 5 i 6 wytypowanych przen nas liczb.\n"
    " W zmiennej o nazwie my_numbers znajduje sie 6 Twoich typowanych liczb od 1 do 49.\n"
    "Wytypuj swoje liczby i sprawdz za ktorym razem wygrasz glowna nagrode"
)
print("\n\n")

date_today = datetime.now()

name = input("Podaj swoje imie: ")

birthday = dateparser.parse(
    input(f"{name} podaj swoja date urodzin rrrr-mm-dd (np. 2000-2-22): ")
)


your_age_days = (date_today - birthday).days
print(f"{name} masz {(your_age_days / 365.25):.0f} lat")
age = int(your_age_days / 365.25)

if age <= 18:
    print(
        f"{name} przykro mi nie jestes osoba dorosla i nie mozesz zagrac w totolotka :("
    )
    exit()
else:
    print(f"{name} masz wystarczajaco lat aby zagrac w totolotka :)")

print("\n\n")
print(
    f"{name} podaj szesc liczby wytypowanych przez Ciebie.\n"
    " Pamietaj ze podane liczby musza byc unikalne czyli nie moga sie powtarzac! \n "
)


my_numbers = set()

while len(my_numbers) != 6:
    my_number = int(input(f"{name} podaj swoja liczbe: "))
    if my_number > 49:
        print(
            f"Podana liczba jest za duza. {name} musisz podac liczbe w przedziale od 1 do 49"
        )
    elif my_number < 1:
        print(
            f"Podana liczba jest za mala. {name} musisz podac liczbe w przedziale od 1 do 49"
        )
    elif my_number in my_numbers:
        print(f"Ta liczba zostala juz wybrana. {name} wybierz inna liczbe")
    else:
        my_numbers.add(my_number)


print(my_numbers)


numbers = list(range(1, 50))


def lottery():
    """"""
    random_numbers = []
    while len(random_numbers) != 6:
        new_number = random.choice(numbers)
        if new_number not in random_numbers:
            random_numbers.append(new_number)
    return random_numbers


if __name__ == "__main__":
    """' efef"""
    i = 1
    proba_6 = 1
    proba_5 = 0
    proba_4 = 0
    proba_3 = 0
    while not set(lottery()).issubset(my_numbers):
        proba_6 += 1
        i += 1
        print(i)
        if len(set(lottery()).intersection(my_numbers)) < 5:
            proba_5 += 1
        # else:
        #     print('masz wygrana! trafile 5')
        if len(set(lottery()).intersection(my_numbers)) < 4:
            proba_4 += 1
        # else:
        #     print('masz wygrana! trafile 4')
        if len(set(lottery()).intersection(my_numbers)) < 3:
            proba_3 += 1
        #     print('masz wygrana! trafile 3')
    else:
        print("wynik:")


czas_wygranej =  round((proba_6 * 7 / 365.25), 2)

print(f"{name } musisz wyslac {proba_6:,} razy kupon aby wygrac glowna wygrana. Bedzie Cie to kosztowac {(proba_6 * 3):,} zl.\n "
        f"Biora pod uwage ze wysylasz jeden kupon tygodniowo, wygranie glownej nagrody zajmie Ci w zaokragleniu {czas_wygranej} lat.\n")
print(f"Podczas wyslania {proba_6:,} kuponow udalo Ci sie trafic {(proba_6 - proba_5):,} razy piatke.\n")
print(f"Podczas wyslania {proba_6:,} kuponow udalo Ci sie trafic {(proba_6 - proba_4):,} razy czworke.\n")
print(f"Podczas wyslania {proba_6:,} kuponow udalo Ci sie trafic {(proba_6 - proba_3):,} razy trojke.\n")
