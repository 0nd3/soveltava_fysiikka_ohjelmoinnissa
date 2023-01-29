"""

tarkastellaan taas jousesta roikkuvaa massaa eulerin menetelmällä, 
mutta otetaan mukaan yksinkertainen malli ilmanvastukselle. 
tällöin diskretoidut yhtälöt voidaan kirjoittaa muotoon

x_new = x + dt * v,
v_new = v + dt * [g - k / m * (x - L) - b / m * v],
x_0 = x~_0,
v_0 = v~_0.

uutta aiempaan verrattuna on siis toisella rivillä termi - b / m * v, missä b on vastuskerroin.


muokkaa tunnilla kirjoitettua koodia "jousi_massa_euler.py" niin, 
että siinä otetaan huomioon myös ilmanvastus.

kokeile ajaa koodi käyttäen parametreina seuraavia:

g = 10
k = 1
m = 1
L = 0
b = 0,25
x_0 = 1
v_0 = 0
t_0 = 0
t_max = 20
dt = 0.01

"""

import matplotlib.pyplot as plt

# määritellään fysikaaliset vakiot

g = 10
k = 1
m = 1
L = 0
b = 0.25

# alkuarvot paikalle ja nopeudelle
x_0 = 1
v_0 = 0

# aikaan liittyvät muuttujat
t_0 = 0
t_max = 20
dt = 0.01

# alustetaan muuttujat
x = x_0
v = v_0
t = t_0

# taulukot muuttujille
x_array = [x_0]
v_array = [v_0]
t_array = [t_0]

# iteroidaan aikaa eteenpäin
while t < t_max:
    # lasketaan uudet arvot
    x_new = x + dt * v
    v_new = v + dt * (g - k/m * (x - L) - b/m * v)
    t_new = t + dt

    # päivitetään
    x = x_new
    v = v_new
    t = t_new

    # lisätään taulukkoon
    x_array.append(x)
    v_array.append(v)
    t_array.append(t)

# luodaan kuvaaja liikkeestä
fig, ax = plt.subplots()
ax.scatter(t_array, x_array)

# lisätään kuvaajan otsikko ja akseleiden nimet
ax.set_xlabel("t")
ax.set_ylabel("x")
ax.set_title("jousi massa euler")

plt.show()