"""

Tarkastellaan logistista rekursiokaavaa

x_new = r * x_n * (1 - x_n),

missä r on jokin reaaliluku ja iteraatio alkaa jostakin alkuarvosta x_0


kirjoita koodi, joka iteroi tätä lauseketta.


tarkista, toimiiko koodisi oikein:

- jos käytetään arvoja r = 1,5 ja x_0 = 0,1, pitäisi olla suurinpiirtein x_11 = 0,3323.
- jos käytetään arvoja r = 2,9 ja x_0 = 0,5, pitäisi olla suurinpiirtein x_50 = 0,6548.

"""

# x alkuarvot
#x_0 = 0.1
x_0 = 0.5

# vakioreaaliluku
#r = 1.5
r = 2.9

# maksimiarvo n;lle
#n_max = 11
n_max = 50

# alustetaan muuttuja x
x = x_0

# luodaan taulukko x:lle
x_array = [x_0]

for n in range(n_max):
    # lasketaan uusi arvo z:lle
    x_new = r * x * (1 - x)

    # päivitetään z
    x = x_new

    # lisätään z taulukkoon
    x_array.append(x)

print(x)