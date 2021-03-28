import math
import random
import seaborn as sns
import matplotlib.pyplot as plt

# functie care calculeaza fitness
def f(x, a, b, c):
    return a*(x**2)+b*x+c


# calcularea lui x din cromozom
def build_x(chromosome, length, a, b):
    x = 0
    for i in range(length-1, -1, -1):
        x += ((2**i)*chromosome[length-i-1])
    return float((b-a)*x/((2**length)-1)+a)


# functie pentru determinarea indivitului elitist
def maxi(fct):
    val = fct[0]
    poz = 0
    i = 0
    for j in fct:
        if val < j:
            val = j
            poz = i
        i += 1
    return val, poz


# functie utilitar de calculare fiecare x si f si afisare
def display_pop(pd, m_tmp, x_tmp, fn_tmp, verbose=True):
    for i in range(pd):
        if verbose:
            g.write(str(i + 1) + ": ")
            for j in m_tmp[i]:
                g.write(str(j))
        x_tmp[i] = build_x(m_tmp[i], l, d, e)
        fn_tmp[i] = f(x_tmp[i], a, b, c)
        if verbose:
            g.write(" x= " + str(x_tmp[i]) + " f= " + str(fn_tmp[i]) + "\n")


# cautarea binara a intervalului corespunzator lui u
def binary_search(interval, low, high, x):
    mid = (high + low) // 2

    # daca x-ul se afla in interval, iar acel interval nu e primul (ca sa nu iasa mid-1 = -1)
    if mid > 0 and interval[mid - 1] <= x < interval[mid]:
        return mid

    # daca x-ul se afla in primul interval
    if mid == 0 and x < interval[mid]:
        return mid
    
    if interval[mid] > x:
        return binary_search(interval, low, mid - 1, x)
    else:
        return binary_search(interval, mid + 1, high, x)


# functie pentru incrucisare
def crossover(chr, ind, verbose=True):
    i = 0
    # daca avem macar 2 cromozomi
    if len(chr) > 1:
        # facem perechi pana ne raman 2 sau 3 cromozomi
        while i + 3 < len(chr):
            # punct de rupere
            break_point = random.randint(0, l - 1)
            if verbose:
                g.write("\nRecombinare dintre cromozomul " + str(ind[i]+1) + " cu cromozomul " + str(ind[i+1]+1) + ":\n")
                for j in chr[i]:
                    g.write(str(j))
                g.write(" ")
                for j in chr[i+1]:
                    g.write(str(j))
                g.write(" punct " + str(break_point) + "\n")
            # print(chr[i], chr[i+1])
            tmp = chr[i][:break_point]
            chr[i] = chr[i+1][:break_point] + chr[i][break_point:]
            chr[i+1] = tmp + chr[i+1][break_point:]
            if verbose:
                g.write("Rezultat     ")
                for j in chr[i]:
                    g.write(str(j))
                g.write(" ")
                for j in chr[i+1]:
                    g.write(str(j))
            # print(chr[i], chr[i+1])
            i += 2
        break_point = random.randint(0, l - 1)
        # daca ne-au ramas 3 cromozomi necombinanti, ii combinam ciclic
        if i + 3 == len(chr):
            # print(chr[i], chr[i+1], chr[i+2])
            if verbose:
                g.write("\nRecombinare dintre cromozomul " + str(ind[i]+1) + " cu cromozomul " + str(ind[i+1]+1) + " si cromozomul " + str(ind[i+2]+1) + ":\n")
                for j in chr[i]:
                    g.write(str(j))
                g.write(" ")
                for j in chr[i+1]:
                    g.write(str(j))
                g.write(" ")
                for j in chr[i+2]:
                    g.write(str(j))
                g.write(" punct " + str(break_point) + "\n")
            tmp = chr[i][:break_point]
            chr[i] = chr[i+1][:break_point] + chr[i][break_point:]
            chr[i+1] = chr[i+2][:break_point] + chr[i+1][break_point:]
            chr[i+2] = tmp + chr[i+2][break_point:]
            # print(chr[i], chr[i+1], chr[i+2])
            if verbose:
                g.write("Rezultat     ")
                for j in chr[i]:
                    g.write(str(j))
                g.write(" ")
                for j in chr[i+1]:
                    g.write(str(j))
                g.write(" ")
                for j in chr[i+2]:
                    g.write(str(j))
        else:
            # daca sunt 2 cromozomi ii facem pereche
            # print(chr[i], chr[i+1])
            if verbose:
                g.write("\nRecombinare dintre cromozomul " + str(ind[i]+1) + " cu cromozomul " + str(ind[i+1]+1) + ":\n")
                for j in chr[i]:
                    g.write(str(j))
                g.write(" ")
                for j in chr[i+1]:
                    g.write(str(j))
                g.write(" punct " + str(break_point) + "\n")
            tmp = chr[i][:break_point]
            chr[i] = chr[i+1][:break_point] + chr[i][break_point:]
            chr[i+1] = tmp + chr[i+1][break_point:]
            # print(chr[i], chr[i+1])
            if verbose:
                g.write("Rezultat     ")
                for j in chr[i]:
                    g.write(str(j))
                g.write(" ")
                for j in chr[i+1]:
                    g.write(str(j))

# citire date
inp = open("date.txt", "r")
# dimensiune populatie
pop_dimension = int(inp.readline())
# print(pop_dimension)
# domeniu de definitie al functiei
domain = inp.readline().split()
d, e = float(domain[0]), float(domain[1])
# print(d, e)
# parametrii functie de grad 2
param = inp.readline().split()
a, b, c = float(param[0]), float(param[1]), float(param[2])
# print(a, b, c)
# precizie
precision = int(inp.readline())
# print(precision)
# probabilitare recombinare
pr = float(inp.readline())
# print(pr)
# probabilitate mutatie
pm = float(inp.readline())
# print(pm)
# nr etape
nr_e = int(inp.readline())
# print(nr_e)

inp.close()

# lungime cromozom
l = math.ceil(math.log((e-d)*(10**precision), 2))
# print(l)

# ca sa obtin acelasi random -- doar pentru testare
# random.seed(123)

# matrice cu cromozomi generati
m = [[random.randint(0, 1) for i in range(l)] for j in range(pop_dimension)]
# for i in range(pop_dimension):
#     print(m[i])


# Afisare populatie initiala
x = [0.0 for i in range(pop_dimension)]
fn = [0.0 for i in range(pop_dimension)]
g = open("evolutie.txt", "w")
g.write("Populatia initiala\n")
display_pop(pop_dimension, m, x, fn)

# determinare individ elitist
val_elite, poz_elite = maxi(fn)
g.write("\nIndivid elitist: " + str(poz_elite+1) + "\n")
elite = m[poz_elite][:]

# probabilitati selectie pentru fiecare cromozom
p = [fn[i]/sum(fn) for i in range(pop_dimension)]
# afisare prob selectie
g.write("\nProbabilitati selectie\n")
for i in range(pop_dimension):
    g.write("cromozom " + str(i+1) + " probabilitate " + str(p[i]) + "\n")
# print(p)

# intervale de selectie
q = [0.0 for i in range(pop_dimension)]
q[0] = p[0]
for i in range(1, pop_dimension):
    q[i] = q[i-1]+p[i]

# afisare intervale probabilitati selectie
g.write("\nIntervale probabilitati selectie\n")
for i in range(pop_dimension):
    g.write(str(q[i]) + " ")

# generare unui numar aleator u si determinarea intervalului caruia apartine
# pe prima pozitie vom pastra individul elitist
m_prim = []  # populatia p'
m_prim.append(elite)
for i in range(pop_dimension-1):
    u = random.uniform(0, 1)
    poz = binary_search(q, 0, pop_dimension-1, u)
    g.write("\nu=" + str(u) + " selectam cromozomul " + str(poz+1))
    m_prim.append(m[poz])

# dupa selectie avem:
g.write("\nDupa selectie:\n")
x_prim = [0.0 for i in range(pop_dimension)]
fn_prim = [0.0 for i in range(pop_dimension)]
display_pop(pop_dimension, m_prim, x_prim, fn_prim)

# participanti incrucisare
g.write("\nProbabilitate de incrucisare " + str(pr) + "\n")
mix = [] # lista de cromozomi care intra la incrucisare
c_nr = [] # indicele "original" al cromozomilor
for i in range(1, pop_dimension):
    g.write(str(i + 1) + ": ")
    for j in m_prim[i]:
        g.write(str(j))
    u = random.uniform(0, 1)
    if u < pr:
        c_nr.append(i)
        mix.append(m_prim[i])
    g.write(" u=" + str(u) + (("<" + str(pr) + " participa") if u < pr else "") + "\n")

# incrucisare
crossover(mix, c_nr)

# dupa incrucisare
g.write("\n\nDupa recombinare:\n")
j = 0
for i in c_nr:
    m_prim[i] = mix[j]
    j += 1
display_pop(pop_dimension, m_prim, x_prim, fn_prim)

# mutatie
g.write("\nProbabilitatea de mutatie pentru fiecare gena " + str(pm))
g.write("\nAu fost modificati cromozomii:")
for i in range(1, pop_dimension):
    u = random.uniform(0, 1)
    if u < pm:
        g.write("\n" + str(i+1))
        poz_elem = random.randint(0, l - 1)
        # calculam complementul
        m_prim[i][poz_elem] = 1 if m_prim[i][poz_elem] == 0 else 0
g.write("\nDupa mutatie:\n")
display_pop(pop_dimension, m_prim, x_prim, fn_prim)


# salvarea datelor pentru plotare
l_maxi = []
l_vmp = []
# evolutie
g.write("\nEvolutie:")
for gen in range(1, nr_e):
    # Actualizare valori pentru fiecare generatie
    m = m_prim
    x = x_prim
    fn = fn_prim

    # determinare individ elitist
    val_elite, poz_elite = maxi(fn)
    elite = m[poz_elite][:]
    # probabilitati selectie pentru fiecare cromozom
    p = [fn[i]/sum(fn) for i in range(pop_dimension)]

    # intervale de selectie
    q = [0.0 for i in range(pop_dimension)]
    q[0] = p[0]
    for i in range(1, pop_dimension):
        q[i] = q[i-1]+p[i]

    # generare unui numar aleator u si determinarea intervalului caruia apartine
    # pe prima pozitie vom pastra individul elitist
    m_prim = []  # populatia p'
    m_prim.append(elite)
    for i in range(pop_dimension-1):
        u = random.uniform(0, 1)
        poz = binary_search(q, 0, pop_dimension-1, u)
        m_prim.append(m[poz])

    # dupa selectie avem:
    x_prim = [0.0 for i in range(pop_dimension)]
    fn_prim = [0.0 for i in range(pop_dimension)]
    display_pop(pop_dimension, m_prim, x_prim, fn_prim, False)

    # participanti incrucisare
    mix = [] # lista de cromozomi care intra la incrucisare
    c_nr = [] # indicele "original" al cromozomilor
    for i in range(1, pop_dimension):
        u = random.uniform(0, 1)
        if u < pr:
            c_nr.append(i)
            mix.append(m_prim[i])

    # incrucisare
    crossover(mix, c_nr, False)
    # dupa incrucisare
    j = 0
    for i in c_nr:
        m_prim[i] = mix[j]
        j += 1
    display_pop(pop_dimension, m_prim, x_prim, fn_prim, False)
    # mutatie
    for i in range(1, pop_dimension):
        u = random.uniform(0, 1)
        if u < pm:
            poz_elem = random.randint(0, l - 1)
            m_prim[i][poz_elem] = 1 if m_prim[i][poz_elem] == 0 else 0
    display_pop(pop_dimension, m_prim, x_prim, fn_prim, False)
    # valuarea maxima
    max_f, temp = maxi(fn_prim)
    # valuarea medie a performantei
    vmp = 0
    for i in range(pop_dimension):
        vmp += fn_prim[i]
    g.write("\nValoare maxima: " + str(max_f) + "     Valoarea medie a performantei: " + str(vmp/pop_dimension))
    l_maxi.append(max_f)
    l_vmp.append(vmp/pop_dimension)
g.close()

# interfata grafica cu evolutia algoritmului
sns.lineplot(data=l_maxi, label="Valoarea maxima")
plt.ylabel('Valoare')
plt.show()
plt.clf()
sns.lineplot(data=l_vmp, label="Valoarea medie a performantei")
plt.ylabel('Valoare')
plt.show()

